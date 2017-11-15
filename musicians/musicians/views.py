# from django.contrib import messages
# from django.core.mail import send_mail
# from django.core.urlresolvers import reverse
# from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView

from .import forms
from bands.models import Album, Artist, Band


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


# class AlbumView(FormView):
#     template_name = 'album_form.html'
#     form_class = forms.AlbumForm
#     success_url = '/album_list/'
#
#     def form_valid(self, form):
#         return super(AlbumView, self).form_valid(form)


class artist_form(CreateView):
    template_name = 'artist_form.html'
    model = Artist
    fields = [
        'first_name',
        'last_name',
        'hometown',
        'twitter_id',
    ]
    template_name_suffix = '_form'
    success_url = '/artist_list/'


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
    ]
    template_name_suffix = '_form'
    success_url = '/band_list/'


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



# def albumform_view(request):
#     form = forms.AlbumForm()
#     if request.method == 'POST':
#         form = forms.AlbumForm(request.POST)
#         if form.is_valid():
#             print("Album Added")
#     return render(request, 'album_form.html', {'form': form})

