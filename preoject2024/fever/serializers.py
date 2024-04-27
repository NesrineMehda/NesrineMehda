from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers

class FeverSerializaers(serializers.ModelSerializer):
      class Meta:
          model = Fever
          fields ='__all__'