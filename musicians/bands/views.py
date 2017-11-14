from django.http import HttpResponse
from django.shortcuts import render

from . models import Band


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
        'band_id': band_id,
    })