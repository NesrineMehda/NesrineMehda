# chat/views.py
from rest_framework import generics
from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer

class RoomListCreateAPIView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class MessageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


