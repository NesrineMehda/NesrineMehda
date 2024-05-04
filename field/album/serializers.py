from rest_framework import serializers
from .models import Album, Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'description', 'image')

class AlbumSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('id', 'title', 'artist', 'release_date', 'photos')
