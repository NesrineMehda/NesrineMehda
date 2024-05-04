from django.urls import path
from .views import AlbumViewSet, PhotoViewSet
from .views import ShowPhoto
urlpatterns = [
    path('album/', AlbumViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('album/<int:pk>/', AlbumViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('album/<int:album_pk>/photos/', PhotoViewSet.as_view({'post': 'create'})),
    path('album/<int:album_pk>/photos/<int:pk>/', PhotoViewSet.as_view({'delete': 'destroy'})),
    path('photos/<int:pk>/', ShowPhoto.as_view(), name='show_photo'),
    
]
