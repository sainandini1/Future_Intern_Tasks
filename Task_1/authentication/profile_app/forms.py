from django.contrib.auth.models import User
from .models import Profile
from django  import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class Register_Form(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

class Login_Form(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username","password"]
class Profile_Form(forms.ModelForm):
    birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Profile
        fields = ["desc","image","name","phone","birth"]