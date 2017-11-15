from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .import forms
from .import models


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
    if request.method == 'POST':
        form = forms.ArtistForm(request.POST)
        if form.is_valid():
            print("Artist Added")
    return render(request, 'artist_form.html', {'form': form})


def bandform_view(request):
    form = forms.BandForm()
    if request.method == 'POST':
        form = forms.BandForm(request.POST)
        if form.is_valid():
                print("Band Added")
    return render(request, 'band_form.html', {'form': form})

class ArtistCreateView(CreateView):
    model = models.Artist


# class artist_form(CreateView):
#     template_name = 'artist_form.html'
#     model = Artist
#     fields = [
#         'first_name',
#         'last_name',
#         'hometown',
#         'twitter_id',
#     ]
#     template_name_suffix = '_form'
#     success_url = '/artist_list/'
#
#
# class band_form(CreateView):
#     template_name = 'band_form.html'
#     model = Band
#     fields = [
#         'members',
#         'name',
#         'genre',
#         'start_date',
#         'end_date',
#         'hometown',
#         'website',
#         'twitter_id',
#     ]
#     template_name_suffix = '_form'
#     success_url = '/band_list/'
#
#
# class album_form(CreateView):
#     template_name = 'album_form.html'
#     model = Album
#     fields = [
#         'band',
#         'name',
#         'create_date',
#     ]
#     template_name_suffix = '_form'
#     success_url = '/album_list/'
#
