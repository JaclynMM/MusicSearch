from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the homepage")

def ArtistDetail(request, artist_id):
    return HttpResponse("Artist Details for" + str(artist_id))

def BandDetail(request, artist_id):
    return HttpResponse("Band Details for" + str(band_id))

def AlbumDetail(request, artist_id):
    return HttpResponse("Album Details for" + str(album_id))