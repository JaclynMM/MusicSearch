from django.conf.urls import include, url
from django.contrib import admin

from . import views
from bands import views as band_views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^artist/$', views.artist_form.as_view(), name='artist_form'),
    url(r'^band/$', views.band_form.as_view(), name='band_form'),
    url(r'^album/$', views.album_form.as_view(), name='album_form'),
    url(r'^search/$', views.search_form_view, name='search'),

    url(r'^band_list/', band_views.band_list, name='band_list'),
    url(r'^artist_list/', band_views.artist_list, name='artist_list'),
    url(r'^album_list/', band_views.album_list, name='album_list'),

    url(r'^artist/(?P<artist_id>[0-9]+)/$', band_views.artist_detail, name='artist_detail'),
    url(r'^band/(?P<band_id>[0-9]+)/$', band_views.band_detail, name='band_detail'),
    url(r'^album/(?P<album_id>[0-9]+)/$', band_views.album_detail, name='album_detail'),

    url(r'^artist_delete/(?P<pk>[0-9]+)/$', views.artist_delete_form.as_view(), name='artist_delete_form'),
    url(r'^band_delete/(?P<pk>[0-9]+)/$', views.band_delete_form.as_view(), name='band_delete_form'),
    url(r'^album_delete/(?P<pk>[0-9]+)/$', views.album_delete_form.as_view(), name='album_delete_form'),

    url(r'^artist_update/(?P<pk>[0-9]+)/$', views.artist_update_form.as_view(), name='artist_update_form'),
    url(r'^band_update/(?P<pk>[0-9]+)/$', views.band_update_form.as_view(), name='band_update_form'),
    url(r'^album_update/(?P<pk>[0-9]+)/$', views.album_update_form.as_view(), name='album_update_form'),


]