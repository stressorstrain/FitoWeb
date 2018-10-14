from django.shortcuts import render
from .models import Gas
from django.core import serializers

json_serializer = serializers.get_serializer("json")()
json_gases = json_serializer.serialize(Gas.objects.all().order_by('id')[:2], ensure_ascii=False)

def post_list(request):
    return render(request, 'gas_control/website.html', {})


def basic(request):
    return render(request, 'gas_control/base.html', {})


def gases(request):
    all_gases = Gas.objects.all()
    for gas in all_gases:
        porc = (100*gas.cvol)/gas.mvol
        gas.porcentage = round(porc, 2)
        gas.save()
    return render(request, 'gas_control/website.html', {'all_gases': all_gases})

# Create your views here.
