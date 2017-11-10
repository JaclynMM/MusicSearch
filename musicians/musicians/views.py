from django.http import HttpResponse
from django.shortcuts import render

from . import forms


def home(request):
    return render(request, 'index.html')
    # return HttpResponse("<h1> Beyond the Band </h1>")


def search_form_view(request):
    form = forms.search_form()
    return render(request, 'search_form.html', {'form'.form})