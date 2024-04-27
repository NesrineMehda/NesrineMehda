from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers

class Userserializer(serializers.ModelSerializer):
      confirm_password= serializers.CharField(write_only=True)

      class Meta:
          model = User 
          fields =['id','firstname' ,'lastname' , 'username' , 'email' ,'password' ,'confirm_password' ] 
          def validate(self ,data):
               if data['password'] != data['confirm_password']:
                 raise serializers.ValidationError('password do not match.')
                 return data 
          def create (self , validate_data):
             validate_data.pop ("confirm_password")     
             return User.objects.create_user(**validate_data)