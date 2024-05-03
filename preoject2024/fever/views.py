from rest_framework.decorators import api_view
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



@api_view(['POST'])
def fever_instance(request, pk):
    try:
        child_instance = Child.objects.get(id=pk)
    except Child.DoesNotExist:
        return Response({"error": "Child with this ID does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    # Extract data from the request
    temperature = request.data.get('temperature')
    fever = request.data.get('fever')
    cough = request.data.get('cough')
    runny_nose = request.data.get('runny_nose')
    difficulty_breathing = request.data.get('difficulty_breathing')
    diarrhea = request.data.get('diarrhea')
    vomiting = request.data.get('vomiting')
    dehydration = request.data.get('dehydration')
    lack_of_activity = request.data.get('lack_of_activity')
    irritability = request.data.get('irritability')
    chronic_diseases = request.data.get('chronic_diseases')
    tummy_ache = request.data.get('tummy_ache')
    others = request.data.get('others')
   
    
    # Categorize fever based on the FeverManager
    fever_result = Fever.objects.categorize_fever(
    temperature,
    child_instance.age_in_days,
    bool(fever),
    bool(cough),
    bool(runny_nose),
    bool(difficulty_breathing),
    bool(diarrhea),
    bool(vomiting),
    bool(dehydration),
    bool(lack_of_activity),
    bool(irritability),
    bool(chronic_diseases),
    bool(tummy_ache),
    others,
)

    # Initialize the serializer with input data and the calculated fever result
    serializer = FeverSerializaers(data={
        "temperature": temperature,
        "fever": fever,
        "cough": cough,
        "runny_nose": runny_nose,
        "difficulty_breathing": difficulty_breathing,
        "diarrhea": diarrhea,
        "vomiting": vomiting,
        "dehydration": dehydration,
        "lack_of_activity": lack_of_activity,
        "irritability": irritability,
        "chronic_diseases": chronic_diseases,
        "tummy_ache": tummy_ache,
        "others": others,
        "fever_duration": fever_duration,  # Include fever_duration
        "diarrhea_duration": diarrhea_duration,  # Include diarrhea_duration
        "result": fever_result
    })
    
    # Validate and save the serializer
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

