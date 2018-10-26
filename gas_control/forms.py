from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Usuarios


class PostForm(forms.Form):
    Ar_Sintético = forms.IntegerField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'style': 'font-size: 70%; width:100%;',
                'placeholder': 'volume em números'
            }
        )
    )
    Hidrogênio = forms.IntegerField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'style': 'font-size: 70%; width:100%;',
                'placeholder': 'volume em números'
            }
        )
    )
    Hélio = forms.IntegerField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'style': 'font-size: 70%; width:100%;',
                'placeholder': 'volume em números'
            }
        )
    )
    Nome_do_Verificador = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'style': 'font-size: 70%; width:100%;',
                'placeholder': 'nome e sobrenome'
            }
        )
    )
    Data_de_Verificacao = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'style': 'font-size: 70%; width:100%;',
                'placeholder': 'dd/mm/aaaa'
            }
        )
    )


class UserForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'style': 'font-size: 70%; width:50%; height:7%; margin-left:24%',
                'placeholder': 'primeiro nome'
            }
        )
    )
    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'style': 'font-size: 70%; width:50%; height:7%; margin-left:24%',
                'placeholder': 'sobrenome'
            }
        )
    )
    username = forms.CharField(
        max_length=12,
        required=True,
        widget=forms.TextInput(
            attrs={
                'style': 'font-size: 70%; width:50%; height:7%; margin-left:24%',
                'placeholder': 'nome de usuário'
            }
        )
    )

    email = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'email@mail.com'
            }
        )
    )
    password2 = forms.CharField(label=("Confirmação de Senha"),
        widget=forms.PasswordInput,
        help_text=(""))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)

