from rest_framework import viewsets
from rest_framework.response import Response
from .models import Album, Photo
from .serializers import AlbumSerializer, PhotoSerializer
from rest_framework import generics
class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class PhotoViewSet(viewsets.ViewSet):
    def create(self, request, album_pk=None):
        album = Album.objects.get(pk=album_pk)
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(album=album)
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    def destroy(self, request, album_pk=None, pk=None):
        try:
            photo = Photo.objects.get(pk=pk, album_id=album_pk)
            photo.delete()
            return Response(status=204)
        except Photo.DoesNotExist:
            return Response(status=404)
    def list(self, request, album_pk=None):
        album = Album.objects.get(pk=album_pk)
        photos = album.photos.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)

    

   
class ShowPhoto(generics.RetrieveAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

