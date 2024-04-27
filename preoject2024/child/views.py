#from django.http  import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializers import *
from .models import *
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def childs(request):
     child =Child.objects.all()
     serializers=ChildSerializaers(child ,many=True)
     return Response(serializers.data) 



@api_view(['POST'])
def addchild(request):
    data = request.data
    serializer = ChildSerializaers(data=data)
    if serializer.is_valid():
        child_instance = serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)



@api_view(['PUT'])
def updatechild(request,pk):
    data= request.data
    child =child.object.get(id=pk)
    serializer=ChildSerializaers(child,data=data)
    if serializer.is_valid():
         serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deletechild(request,pk):
    child  =Child.objects.get(id=pk)
    child.delete()   
    return Response('Note was deleted')


