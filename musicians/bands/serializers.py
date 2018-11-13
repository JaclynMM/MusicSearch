from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Band, Artist, Album


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ('first_name', 'last_name', 'hometown', 'twitter_id', 'id')

class BandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Band
        fields = ('members', 'name', 'genre', 'start_date', 'end_date', 'hometown', 'website', 'twitter_id', 'id')

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ('band', 'name', 'create_date', 'id')