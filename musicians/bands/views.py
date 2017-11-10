from django.http import HttpResponse

from . models import Artist


def home(request):
    return HttpResponse("<h1> This is the homepage </h1>")

def ArtistDetail(request, artist_id):
    return HttpResponse("<h2> Artist Details for " + str(artist_id) + "</h2>")

def BandDetail(request, band_id):
    return HttpResponse("<h2> Band Details for " + str(band_id) + "</h2>")

def AlbumDetail(request, album_id):
    return HttpResponse("<h2> Album Details for " + str(album_id) + "</h2>")

