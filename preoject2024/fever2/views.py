from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response 
from .serializers import *
from .models import *
from childs.models  import *
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def fever(request):
     fever  =Fever.objects.all()
     serializers=FeverSerializaers(fever ,many=True)
     return Response(serializers.data) 

class Fever_instance(APIView):
    def post(self, request):
        try:
            serializer = FeverSerializaers(data=request.data)
            if serializer.is_valid():
                fever = serializer.save()
                result = fever.fever_instance()
                return Response({"result": result, "message": "This is correct"}, status=status.HTTP_201_CREATED) 
            return Response({"message": "This is incorrect"}, serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e), "message": "This is incorrect01"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

