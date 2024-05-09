

from django.contrib.auth.models import User
from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.value



