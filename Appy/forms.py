from django import forms
from .models import Products
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# The creation form of django like in cmd has 3 fields only, therefore email addition through extension
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text="Please enter valid email")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        # fields = "__all__"



class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ["name","description","price","category","image"]
        # fields = "__all__"


