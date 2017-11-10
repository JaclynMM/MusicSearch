from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^search_form/$', views.search_form_view, name='search_form'),
    url(r'^bands/', include('bands.urls')),

]