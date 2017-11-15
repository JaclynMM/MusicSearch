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


def artist_detail(request, artist_id):
    get_artist = Artist.objects.get(id=artist_id)
    return render(request, 'ArtistDetail.html', {
        'artist': get_artist,
    })


def album_detail(request, album_id):
    get_album = Album.objects.get(id=album_id)
    return render(request, 'AlbumDetail.html', {
        'album': get_album,
    })


def band_list(request):
    get_band = Band.objects.all()
    print(get_band)
    return render(request, 'band_list.html', {
        'bands': get_band,
    })


def artist_list(request):
    get_artist = Artist.objects.all()
    print(get_artist)
    return render(request, 'artist_list.html', {
        'artists': get_artist,
    })


def album_list(request):
    get_album = Album.objects.all()
    print(get_album)
    return render(request, 'album_list.html', {
        'albums': get_album,
    })
