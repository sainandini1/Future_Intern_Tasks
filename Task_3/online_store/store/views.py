from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, CartItem, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Product List View
def product_list(request):
    products = Product.objects.all()

    # Sorting
    sort_by = request.GET.get('sort_by')
    if sort_by in ['price', 'name']:
        products = products.order_by(sort_by)

    # Filtering by name
    name = request.GET.get('name')
    if name:
        products = products.filter(name__icontains=name)

    # Filtering by price range
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    if price_min and price_max:
        products = products.filter(price__gte=price_min, price__lte=price_max)
    elif price_min:
        products = products.filter(price__gte=price_min)
    elif price_max:
        products = products.filter(price__lte=price_max)

    context = {
        'products': products
    }
    return render(request, 'product_list.html', context)

# Product Detail View
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            messages.success(request, 'Review added successfully!')
            return redirect('product_detail', pk=pk)
    else:
        form = ReviewForm()

    return render(request, 'product_detail.html', {'product': product, 'reviews': reviews, 'form': form})

# Add to Cart View
@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    quantity = int(request.POST.get('quantity', 1))
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity

    cart_item.save()
    messages.success(request, f'{product.name} added to cart.')
    return redirect('cart_detail')

# Cart Detail View
@login_required
def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    if not cart_items:
        messages.info(request, 'Your cart is empty.')

    return render(request, 'cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})

# Edit Cart Item View
@login_required
def edit_cart_item(request, item_id):
    if request.method == "POST":
        quantity = request.POST.get("quantity")
        cart_item = get_object_or_404(CartItem, user=request.user, product__id=item_id)
        cart_item.quantity = int(quantity)
        cart_item.save()
        messages.success(request, 'Cart item updated.')
        return redirect('cart_detail')

    # If not POST, redirect to the cart detail page
    return redirect('cart_detail')

# Delete Cart Item View
@login_required
def delete_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, user=request.user, product__id=item_id)
    cart_item.delete()
    messages.success(request, 'Cart item deleted.')
    return redirect('cart_detail')

# Signup View
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('signup')
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        messages.success(request, 'Signup successful! You can now log in.')
        return redirect('login')
    return render(request, 'signup.html')

# Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Login successful! Welcome, {username}.')
            return redirect('product_list')
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')
    return render(request, 'login.html')

# Logout View
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')
