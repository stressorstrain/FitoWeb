from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from .accoutns_choices import *
from django.db import models


class CustomAuthForm(forms.Form):
    username = forms.CharField(
        label='Username',
        required=True,
        widget=TextInput(
            attrs={'style': 'font-size: 120%; width:50%; height:10%; margin-left:24%',
                   }
        )
    )
    password = forms.CharField(
        label='Senha',
        required=True,
        widget=PasswordInput(
            attrs={'style': 'font-size: 120%; width:50%; height:2%; margin-left:24%',
                   }
        )
    )


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        label="Nome",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'style': 'font-size: 120%; width:50%; height:7%; margin-left:24%',
            }
        )
    )
    last_name = forms.CharField(
        label='Sobrenome',
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'style': 'font-size: 120%; width:50%; height:7%; margin-left:24%',
            }
        )
    )
    email = forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'email@mail.com'
            }
        )
    )
    username = forms.CharField(
        max_length=24,
        required=True,
        widget=TextInput(
            attrs={'style': 'font-size: 120%; width:50%; height:7%; margin-left:24%',
                   }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):

    avatar = forms.ImageField(required=True)

    class Meta:
        model = UserProfile
        fields = ('avatar',)