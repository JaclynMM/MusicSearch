from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .import forms
from bands.models import Album, Artist, Band
from django.core import serializers


def home(request):
    return render(request, 'home.html')


#Search Bar
def search_form_view(request):
    query = request.GET.get("q")
    artists = Artist.objects.filter(last_name=query)
    bands = Band.objects.filter(name=query)
    return render(request, 'search_results.html', {'artists': artists, 'bands': bands})

def artist_search_view(request):
    query = request.GET.get("q")
    artists = Artist.objects.filter(last_name=query)
    data = serializers.serialize ("json", artists)
    return HttpResponse (data, content_type="application/json")

def artist_search_id_view(request):
    query = request.GET.get("id")
    artists = Artist.objects.filter(id=query)
    data = serializers.serialize ("json", artists)
    return HttpResponse (data, content_type="application/json")

def band_search_view(request):
    query = request.GET.get("q")
    bands = Band.objects.filter(name=query)
    data = serializers.serialize ("json", bands)
    return HttpResponse (data, content_type="application/json")

def band_search_id_view(request):
    query = request.GET.get("id")
    bands = Band.objects.filter(id=query)
    data = serializers.serialize ("json", bands)
    return HttpResponse (data, content_type="application/json")


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


#Artist Model Views
class artist_form(CreateView):
    template_name = 'artist_form.html'
    model = Artist
    fields = [
        'first_name',
        'last_name',
        'hometown',
        'twitter_id',
        'id',
    ]
    template_name_suffix = '_form'
    success_url = '/artist_list/'


class artist_delete_form(DeleteView):
    template_name = 'artist_confirm_delete.html'
    model = Artist
    success_url = '/artist_list/'


class artist_update_form(UpdateView):
    template_name = 'artist_update_form.html'
    model = Artist
    fields = [
        'first_name',
        'last_name',
        'hometown',
        'twitter_id',
        'id',
    ]
    success_url = '/artist_list/'


#Band Model Views
class band_form(CreateView):
    template_name = 'band_form.html'
    model = Band
    fields = [
        'members',
        'name',
        'genre',
        'start_date',
        'end_date',
        'hometown',
        'website',
        'twitter_id',
        'id',
    ]
    template_name_suffix = '_form'
    success_url = '/band_list/'


class band_delete_form(DeleteView):
    template_name = 'band_confirm_delete.html'
    model = Band
    success_url = '/band_list/'


class band_update_form(UpdateView):
    template_name = 'band_update_form.html'
    fields = [
        'members',
        'name',
        'genre',
        'start_date',
        'end_date',
        'hometown',
        'website',
        'twitter_id',
    ]
    model = Band
    success_url = '/band_list/'


#Album Model Views
class album_form(CreateView):
    template_name = 'album_form.html'
    model = Album
    fields = [
        'band',
        'name',
        'create_date',
    ]
    template_name_suffix = '_form'
    success_url = '/album_list/'


class album_delete_form(DeleteView):
    template_name = 'album_confirm_delete.html'
    model = Album
    success_url = '/album_list/'


class album_update_form(UpdateView):
    template_name = 'album_update_form.html'
    model = Album
    fields = [
        'band',
        'name',
        'create_date',
    ]
    success_url = '/album_list/'
