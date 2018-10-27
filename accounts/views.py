from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomAuthForm
from .forms import UserForm
from django.contrib.auth.models import User
# Create your views here.


def log_in(request):
    form = CustomAuthForm()
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'accounts/profile.html', {})

    else:
        messages.error(request, "Error wrong username/password")
    return render(request, "registration/login.html", {'form': form})


def profile(request):
    print("profile")
    return render(request, 'accounts/profile.html', {})


def log_out(request):
    logout(request)
    return render(request, 'base.html', {})


def basic(request):
    return render(request, 'base.html', {})


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        form2 = CustomAuthForm()
        if form.is_valid():
            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username, email, password1)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        return render(request, 'registration/login.html', {'form': form2})

    else:
        form = UserForm()

        return render(request, 'accounts/userc.html', {'form': form})

