from django.conf.urls import include, url
from django.contrib import admin

from . import views
from bands import views as band_views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Artist', band_views.ArtistViewSet)
router.register(r'Band', band_views.BandViewSet)
router.register(r'Album', band_views.AlbumViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^home/', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^artist/$', views.artist_form.as_view(), name='artist_form'),
    url(r'^band/$', views.band_form.as_view(), name='band_form'),
    url(r'^album/$', views.album_form.as_view(), name='album_form'),
    url(r'^search/$', views.search_form_view, name='search'),
    url(r'^artist-search/$', views.artist_search_view, name='searchArtist'),
    url(r'^band-search/$', views.band_search_view, name='searchBand'),
    url(r'^artist-search-id/$', views.artist_search_id_view, name='searchArtistbyID'),
    url(r'^band-search-id/$', views.band_search_id_view, name='searchBandbyID'),



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