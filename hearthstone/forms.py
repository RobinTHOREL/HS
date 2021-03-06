from django import forms
from django.contrib.auth.models import User
from hearthstone.models  import Deck
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        help_texts = {
            'username': None,
            'email': None, 
            'password1': "test",
            'password2': "test",
        }
        fields = ['username', 'email', 'password1', 'password2']
