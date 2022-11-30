from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import *


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email', 'profile_pic', 'faculty']


# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2']
