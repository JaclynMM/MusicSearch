from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),

    #/bands/71/
    url(r'^(?P<band_id>[0-9]+)/$', views.band_detail, name='band_detail'),
]
