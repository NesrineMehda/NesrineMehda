from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers

class VaccinSerializers(serializers.ModelSerializer):
      class Meta:
          model = Vaccin 
          fields ='__all__' 