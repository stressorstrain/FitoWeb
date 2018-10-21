from django.shortcuts import render
from .models import Gas
from django.core import serializers
from .forms import PostForm
from django.http import JsonResponse

json_serializer = serializers.get_serializer("json")()
json_gases = json_serializer.serialize(Gas.objects.all().order_by('id'), ensure_ascii=False)


def post_new(request):
    return render(request, 'gas_control/gas.html', )


def basic(request):
    return render(request, 'gas_control/base.html', {})


def chart(request):
    return render(request, 'gas_control/chart.html', {})


def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) #http response


def gases(request):
    all_gases = Gas.objects.all().order_by('-id')[:3]
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['Gas']
            cvol = form.cleaned_data['Volume_Verificado']
            porcentage = porcentagem(name, cvol)
            ver_name = form.cleaned_data['Nome_do_Verificador']
            ver_date = form.cleaned_data['Data_de_Verificacao']
            data = Gas(name=name, cvol=cvol, porcentage=porcentage, ver_name=ver_name, ver_date=ver_date)
            data.save()
            return render(request, 'gas_control/website.html', {'all_gases': all_gases, 'form': form})

    else:
        form = PostForm
        return render(request, 'gas_control/website.html', {'all_gases': all_gases, 'form': form})


def porcentagem(name,cvol):
    ars = ['Ar Sintético', 'Ar Sintetico', 'ar sintético', 'ar sintetico']
    h2 = ['Hidrogênio', 'Hidrogenio', 'hidrogenio', 'hidrogênio']
    he = ['Hélio', 'Helio', 'hélio', 'helio']
    if name in ars:
        mvol = 18000
        return(cvol*100)/mvol
    elif name in h2:
        mvol = 16000
        return(cvol*100)/mvol
    elif name in he:
        mvol = 150
        return(cvol*100)/mvol
