from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Gas, Usuarios
from django.core import serializers
from .forms import PostForm, UserForm, UserCreationForm
from django.http import JsonResponse
from .gas import *
json_serializer = serializers.get_serializer("json")()
json_gases = json_serializer.serialize(Gas.objects.all().order_by('id'), ensure_ascii=False)


def post_new(request):
    return render(request, 'gas_control/gas.html', )


def basic(request):
    return render(request, 'gas_control/base.html', {})


def chart(request):
    return render(request, 'gas_control/chart.html', {})


def gases(request):
    all_gases = Gas.objects.all().order_by('-id')[:1]

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            #name = form.cleaned_data['Gas']
            #cvol = form.cleaned_data['Volume_Verificado']
            ars = form.cleaned_data['Ar_Sintético']
            ars_p = porcentagem(ars, 'ars')
            h2 = form.cleaned_data['Hidrogênio']
            h2_p = porcentagem(h2, 'h2')
            he = form.cleaned_data['Hélio']
            he_p = porcentagem(he, 'he')
            ver_name = form.cleaned_data['Nome_do_Verificador']
            ver_date = form.cleaned_data['Data_de_Verificacao']
            info = (str(ver_date)+"\t"+str(ars)+"\t"+str(h2)+"\t"+str(he))
            start(info)
            data = Gas(ars=ars, h2=h2, he=he, ars_p=ars_p, h2_p=h2_p, he_p=he_p, ver_name=ver_name, ver_date=ver_date)
            data.save()

            return render(request, 'gas_control/website.html', {'all_gases': all_gases,'form': form})

    else:

        form = PostForm
        return render(request, 'gas_control/website.html', {'all_gases': all_gases, 'form': form})


def porcentagem(cvol, ind):
    ars = ['Ar Sintético', 'Ar Sintetico', 'ar sintético', 'ar sintetico', 'ars']
    h2 = ['Hidrogênio', 'Hidrogenio', 'hidrogenio', 'hidrogênio', 'h2']
    he = ['Hélio', 'Helio', 'hélio', 'helio', 'he']
    if ind in ars:
        mvol = 18000
        return(cvol*100)/mvol
    elif ind in h2:
        mvol = 16000
        return(cvol*100)/mvol
    elif ind in he:
        mvol = 150
        return(cvol*100)/mvol


def register(request):


    if request.method == "POST":

        form = UserForm(request.POST)

        if form.is_valid():
            print("é sim po")
            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            form.save()
            return redirect('/')

    else:
        form = UserForm()

        return render(request, 'gas_control/userc.html',{'form': form})








