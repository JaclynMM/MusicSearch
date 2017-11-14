from django.http import HttpResponse
from django.shortcuts import render

from .import forms


def home(request):
    return render(request, 'home.html')


def search_form_view(request):
    search_bar = SearchBar(request, ['name'])
    if search_bar.is_valid():
        return render(request, 'django_searchbar/home.html', {'search_bar': search_bar,})
    else:
        return HttpResponse('We could not locate that search.')


def artistform_view(request):
    form = forms.ArtistForm()
    return render(request, 'artist_form.html', {'form': form})
