# # from django.conf.urls import url
# from django.conf.urls import url, include

# from rest_framework import routers
# from musicians import views

# router = routers.DefaultRouter()
# router.register(r'Artist2', views.ArtistViewSet)
# router.register(r'Band', views.BandViewSet)
# router.register(r'Album', views.AlbumViewSet)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     url(r'^', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

# #
# # from . import views
# #
# # urlpatterns = [
# #     url(r'^$', views.home, name='home'),
# #
# #     url(r'^(?P<artist_id>[0-9]+)/$', views.artist_list, name='artist_detail'),
# #     # url(r'^(?P<band_id>[0-9]+)/$', views.band_detail, name='band_detail'),
# #     # url(r'^(?P<album_id>[0-9]+)/$', views.album_list, name='album_detail'),
# #
# # ]
