# from django.contrib import messages
# from django.core.mail import send_mail
# from django.core.urlresolvers import reverse
# from django.http import HttpResponseRedirect
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
    if request.method == 'POST':
        form = forms.ArtistForm(request.POST)
        if form.is_valid():
            print("Artist Added")
            # to send info in to email
            # send_mail(
            #     'Artist from {}'.format(form.cleaned_data['name']),
            #     form.cleaned_data['Band'],
            #     form.cleaned_data['Name'],
            #     form.cleaned_data['Create Date'],
            #     ['jaclyn.mullin@gmail.com']
            # )
            # messages.add_message(request, messages.SUCCESS,
            #                      'Thank you for your expertise. '
            #                      'Our team will review your input and add do the database for others to enjoy')
            # return HttpResponseRedirect('artist_form')
    return render(request, 'artist_form.html', {'form': form})


def bandform_view(request):
    form = forms.BandForm()
    if request.method == 'POST':
        form = forms.BandForm(request.POST)
        if form.is_valid():
                print("Band Added")
    return render(request, 'band_form.html', {'form': form})


def albumform_view(request):
    form = forms.AlbumForm()
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            print("Album Added")
    return render(request, 'album_form.html', {'form': form})

