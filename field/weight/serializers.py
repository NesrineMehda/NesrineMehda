from rest_framework import serializers

class CalculateBMISerializer(serializers.Serializer):
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    height = serializers.FloatField()
