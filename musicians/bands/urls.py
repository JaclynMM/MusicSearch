from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    #artist_id page
    url(r'^(?P<artist_id>[0-9]+)/$', views.ArtistDetail, name='ArtistDetail'),

    #band_id page
    url(r'^(?P<band_id>[0-9]+)/$', views.BandDetail, name='BandDetail'),

    #album page
    url(r'^(?P<album_id>[0-9]+)/$', views.AlbumDetail, name='AlbumDetail'),

]
