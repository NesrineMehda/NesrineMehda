from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializers import *
from .models import *
from child.models  import *
from rest_framework import status
from django.shortcuts import get_object_or_404



@api_view(['GET'])
def fever(request):
     fever =Fever.objects.all()
     serializers=FeverSerializaers(fever ,many=True)
     return Response(serializers.data)


@api_view(['GET'])
def fever_instanc1e(request, pk):
    try:
        child_instance = Child.objects.get(id=pk)
    except Child.DoesNotExist:
        return Response({"error": "Child with this ID does not exist"}, status=404)
    
    fever = Fever.objects.categorize_fever(request.temperature,child_instance, request.data.fever, request.data.cough, request.data.runny_nose,request.data.difficulty_breathing, request.data.diarrhea, request.data.vomiting, request.data.dehydration, request.data.lack_of_activity, request.data.irritability, request.data.others)
    
    serializer = FeverSerializaers(fever)
    return Response(serializer.data)

@api_view(['POST'])
def fever_instance(request, pk):
    try:
        child_instance = Child.objects.get(id=pk)
    except Child.DoesNotExist:
        return Response({"error": "Child with this ID does not exist"}, status=404)
    
    fever = Fever.objects.categorize_fever(
        request.data.get('temperature'),
        child_instance.age_in_days(),
        request.data.get('fever'),
        request.data.get('cough'),
        request.data.get('runny_nose'),
        request.data.get('difficulty_breathing'),
        request.data.get('diarrhea'),
        request.data.get('vomiting'),
        request.data.get('dehydration'),
        request.data.get('lack_of_activity'),
        request.data.get('irritability'),
        request.data.get('others'),
        
    ) 
   
    serializer = FeverSerializaers(data={"temperature": request.data.get('temperature'), 
     "fever": request.data.get('fever'), "cough": request.data.get('cough'), "runny_nose": request.data.get('runny_nose'),
     "difficulty_breathing": request.data.get('difficulty_breathing'), "diarrhea": request.data.get('diarrhea'), 
     "vomiting": request.data.get('vomiting'), "dehydration": request.data.get('dehydration'), 
     "lack_of_activity": request.data.get('lack_of_activity'), "irritability": request.data.get('irritability'), 
     "others": request.data.get('others'), "result": fever})#
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
