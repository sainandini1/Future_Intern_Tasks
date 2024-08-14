from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import forms
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseForbidden
 
def custom_404(request, exception=None):
    return render(request, '404.html', status=404)

def home(request):
   
   
    return render(request,"profile_app/index.html")


def register_view(request):
     if request.method == "POST":
        form = forms.Register_Form(request.POST)
        if form.is_valid():
            user =form.save()
            login(request,user)
            return redirect("home")
        else:
           return render(request,"profile_app/register.html",{"form":form})
     form = forms.Register_Form()
     
     return render(request,"profile_app/register.html",{"form":form})
 
def login_view(request):
    
    if request.method == "POST":
        form = forms.Login_Form(request,data=request.POST)
        if form.is_valid():
            user =form.get_user()
            login(request,user)
            return redirect("home")
        else:
            error= "Please Check Inputs !"
            return render(request,"profile_app/login.html",{"form":form,"error":error})
    form = forms.Login_Form()
    return render(request,"profile_app/login.html",{"form":form})
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")

@login_required
def profile_update(request):
    if not request.user.has_perm('some_permission'):
        return render(request,"profile_app/403.html")
    # Your view logic here
     
    profile =request.user.profile
    if request.method == "POST":
        form = forms.Profile_Form(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request,"profile_app/profile_form.html",{"form":form})
    else:
        form = forms.Profile_Form(instance=profile)
        return render(request,"profile_app/profile_form.html",{"form":form,"profile":profile})    

def profile_view(request):
    if not request.user.is_authenticated:
        return render(request, "profile_app/403.html")

    profile = request.user.profile
        
    return render(request,"profile_app/profile.html",{"profile":profile})
def delete_view(request):
    user=request.user
    if request.method == "POST":
       user.delete()
       logout(request)
       return redirect("home")
    