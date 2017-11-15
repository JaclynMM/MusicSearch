from django.conf.urls import include, url
from django.contrib import admin

from . import views
from bands import views as band_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^artist/$', views.artistform_view, name='artist_form'),
    url(r'^band/$', views.bandform_view, name='band_form'),
    url(r'^album/$', views.albumform_view, name='album_form'),

    url(r'^artist_list/$', band_views.artist_list, name='artist_list'),

    url(r'^band_list/', include('bands.urls'), name='band_list'),
    url(r'^album_list/', include('bands.urls'), name='album_list'),

]