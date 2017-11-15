from django.http import HttpResponse
from django.shortcuts import render

from .models import Band, Artist, Album


def home(request):
    all_bands = Band.objects.all()
    return render(request, 'band_list.html', {
        'bands': all_bands,
    })
    # html = ''
    # for band in all_bands:
    #     url = '/bands/' + str(band.id) + '/'
    #     html += "<a href = " ' + url + ' "> ' + band.band_name' </a> <br>"
    # return HttpResponse(html)


def band_detail(request, band_id):
    get_band = Band.objects.get(id=band_id)
    return render(request, 'BandDetail.html', {
        'band': get_band,
    })


def artist_list(request, artist_id):
    get_artist = Artist.objects.get(id=artist_id)
    return render(request, 'ArtistDetail.html', {
        'artist': get_artist,
    })


def album_list(request, album_id):
    get_album = Album.objects.get(id=album_id)
    return render(request, 'AlbumDetail.html', {
        'album': get_album,
    })
