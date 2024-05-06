from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers

class ChildSerializaers(serializers.ModelSerializer):
      class Meta:
          model = Child 
          fields ='__all__' 








        