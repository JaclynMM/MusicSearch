from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^artist/$', views.artistform_view, name='artist_form'),
    url(r'^band_list/', include('bands.urls')),

]