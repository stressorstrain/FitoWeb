from django.shortcuts import render
from . import gas
from .models import Gas
from django.core import serializers
from .forms import PostForm
from .gas import *
from django.contrib.auth.decorators import login_required
json_serializer = serializers.get_serializer("json")()
#json_gases = json_serializer.serialize(Gas.objects.all().order_by('id'), ensure_ascii=False)


def post_new(request):
    return render(request, 'gas_control/gas.html', )


def basic(request):
    return render(request, 'base.html', {})


def chart(request):
    return render(request, 'gas_control/chart.html', {})


@login_required
def gases(request):
    all_gases = Gas.objects.all().order_by('-id')[:1]
    last_check = Gas.objects.latest('id').ver_date
    last_checker = Gas.objects.latest('id').ver_name
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            ars = form.cleaned_data['Ar_Sintético']
            ars_p = porcentagem(ars, 'ars')
            h2 = form.cleaned_data['Hidrogênio']
            h2_p = porcentagem(h2, 'h2')
            he = form.cleaned_data['Hélio']
            he_p = porcentagem(he, 'he')
            ver_name = form.cleaned_data['Nome_do_Verificador']
            ver_date = form.cleaned_data['Data_de_Verificacao']
            new_data = (str(ver_date)+"\t"+str(ars)+"\t"+str(h2)+"\t"+str(he))
            gas.start(new_data)
            data = Gas(ars=ars, h2=h2, he=he, ars_p=ars_p, h2_p=h2_p, he_p=he_p, ver_name=ver_name, ver_date=ver_date)
            data.save()

            return render(request, 'gas_control/website.html',
                          {
                              'all_gases': all_gases,
                              'form': form,
                              'last_check': last_check,
                              'last_checker': last_checker
                          })

    else:

        form = PostForm
        return render(request, 'gas_control/website.html',
                      {
                          'all_gases': all_gases,
                          'form': form,
                          'last_check': last_check,
                          'last_checker': last_checker
                      })


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
