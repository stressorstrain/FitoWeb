from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomAuthForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget=TextInput(
            attrs={'style': 'font-size: 70%; width:50%; height:10%; margin-left:24%',
                   }
        )
    )
    password = forms.CharField(
        required=True,
        widget=PasswordInput(
            attrs={'style': 'font-size: 70%; width:50%; height:2%; margin-left:24%',
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
    password2 = forms.CharField(
                                label="Confirmação de Senha",
                                widget=forms.PasswordInput,
                                help_text=""
                                )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)
