from django.http import HttpResponse

from . models import Band


def home(request):
    all_bands = Band.objects.all()
    html = ''
    for band in all_bands:
        url = '/bands/' + str(band_id) + '/'
        html += "<a herf = " ' + url + ' "> ' + band.band_name' </a> <br>"
    return HttpResponse(html)

def band_detail(request, band_id):
    return HttpResponse("<h2>Details for Band Id:" + str(band_id) + "</h2>")
