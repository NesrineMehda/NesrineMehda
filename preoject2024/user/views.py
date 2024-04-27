from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Userserializer
from rest_framework.decorators import api_view
from .models import *

 
@api_view(['GET'])
def getUsers(request):
     user =User.objects.all()
     serializers=Userserializer(user,many=True)
     return Response(serializers.data)

class SignUpView(APIView):
    def post(self, request):
        serializer = Userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Usqer created successfuly'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

