from django.shortcuts import render, redirect


def basic(request):
    return render(request, 'base.html', {})