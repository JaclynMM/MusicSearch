from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^(?P<band_id>[0-9]+)/$', views.band_detail, name='band_detail'),
    url(r'^(?P<artist_id>[0-9]+)/$', views.artist_list, name='artist_detail'),
    url(r'^(?P<album_id>[0-9]+)/$', views.album_list, name='album_detail'),

]
