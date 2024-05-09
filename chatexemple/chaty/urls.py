
from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.RoomListCreateAPIView.as_view(), name='room-list-create'),
    path('messages/', views.MessageListCreateAPIView.as_view(), name='message-list-create'),
]

