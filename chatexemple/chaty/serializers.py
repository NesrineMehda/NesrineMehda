
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Room, Message

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name']



class MessageSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ['id', 'value', 'date', 'user', 'room']

    def create(self, validated_data):
        room_name = validated_data.pop('room')
        user_id = validated_data.pop('user').id  # Fetch the user id
        
        # Fetch or create the room
        room, _ = Room.objects.get_or_create(name=room_name)

        # Fetch the user
        user = User.objects.get(pk=user_id)

        # Create the message
        message = Message.objects.create(room=room, user=user, **validated_data)
        return message
