from django.http import HttpResponse
from django.shortcuts import render

from . import forms


def home(request):
    # return render(request, 'index.html')
    return HttpResponse("<h1> Beyond the Band </h1>")


def search_view(request):
    if request.method == 'GET':
        form = forms.search_form(request.POST)
        if form.is_valid():
            return render(request, artist_name, {'form':form})
    else:
        return HttpResponse('We could not locate that search.')

