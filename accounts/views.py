from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomAuthForm, RegistrationForm, ProfileForm
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your views here.


def log_in(request):
    template = 'registration/login.html'
    user_req = request.user
    if user_req.is_authenticated:
        username = user_req.username
        return redirect('accounts:profilepage', username)
    else:
        form = CustomAuthForm()
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            name = user.first_name + "_" + user.last_name
            return redirect('accounts:profilepage', username)

        else:
            messages.error(request, "Error wrong username/password")
        return render(request, "registration/login.html", {'form': form})


def profile(request, username):
    all_profiles =  UserProfile.objects.all()
    all_users = User.objects.all()
    return render(request, 'accounts/profile.html', {'users': all_users, 'profiles': all_profiles, 'username': username})


def log_out(request):
    logout(request)
    return render(request, 'base.html', {})


def redirector(request):
    model = User
    slug_field = "username"
    template_name = 'accounts/profile.html'


def register(request):
    if request.method == "POST":
        form1 = RegistrationForm(request.POST)
        form2 = ProfileForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            username = form1.cleaned_data['username']
            raw_password = form1.cleaned_data['password1']
            user.set_password(raw_password)
            user.save()

            avatar = form2.cleaned_data["avatar"]
            profile = UserProfile(user=user, avatar=avatar)
            profile.save()


        else:
            print("not valid")

        return redirect('accounts:login')

    else:
        form = RegistrationForm()
        form2 = ProfileForm()
        print("k")
        return render(request, 'accounts/userc.html', {'form': form, 'form2':form2})


def user_page(request, user_id):
    pass
