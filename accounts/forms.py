from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, UserProjects, UserUploads, UserDates
from .accoutns_choices import *
import datetime
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


class ProjectsForm(forms.Form):
    projeto = forms.CharField(
        max_length=200,
        label='Nome Do Projeto',
        required=True,
        widget=TextInput(
            attrs={'style': 'font-size: 120%; width:100%; height:10%;',
                   }
        )
    )
    data = forms.CharField(
        max_length=200,
        label='Data de Execução',
        required=True,
        widget=TextInput(
            attrs={'style': 'font-size: 120%; width:100%; height:10%;',
                   }
        )
    )
    nivel = forms.ChoiceField(
        choices=NIVEL_CHOICES,
        required=True,
        widget=forms.Select(
            attrs={
                'style': 'font-size: 120%; width:100%; height:7%; '}
        )
    )

    class Meta:
        model: UserProjects
        fields = ('projeto', 'data', )


class UserUploadsForms(forms.Form):
    docname = forms.CharField(
        max_length=30,
        label='Nome do Documento',
        required=True,
        widget=TextInput(
            attrs={'style': 'font-size: 100%; width:100%; height:10%;',
                   }
        )

    )

    file = forms.FileField()
    type = forms.ChoiceField(
        choices=DOC_TYPES,
        label = 'Tipo de Arquivo',
        required=True,
        widget=forms.Select(
            attrs={
                'style': 'font-size: 80%; width:100%; height:7%; '}
        )
    )
    projetos = forms.CharField(
        max_length=30,
        label='Selecione o Projeto',
        required=True,
        widget=TextInput(
            attrs={'style': 'font-size: 100%; width:100%; height:6%; background: grey','readonly':'readonly',
                   }
        )

    )
    class Meta:
        model: UserUploads
        fields = ('projetos', 'docname', 'file', 'type')


class NotesForm(forms.Form):
    note_text = forms.CharField(
        max_length=1000,
        required=True,
        label='Nota:',

    )
    note_date = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=TextInput(
            attrs={
                'readonly':'readonly'
            }
        )
    )

    class Meta:
        model: UserDates
        fields = ('note_text', )


class FilesForm(forms.Form):

    file = forms.FileField()
    type = forms.ChoiceField(
        choices=DOC_TYPES,
        required=True,
        widget=forms.Select(
            attrs={
                'style': 'font-size: 80%; width:50%; height:7%; margin-left:24%'}
        )
    )


