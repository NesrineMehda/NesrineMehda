#from django.http  import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializers import *
from .models import *
from rest_framework import status
from django.shortcuts import get_object_or_404
from child.models import Child

@api_view(['GET'])
def nearest_vaccine__all(request, pk):
    try:
        child_instance = Child.objects.get(id=pk)
    except Child.DoesNotExist:
        return Response({"error": "Child with this ID does not exist"}, status=404)
    
    nearest_vaccine = Vaccin.objects.nearest_vaccine_for_child(child_instance)
    serializer = VaccinSerializers(nearest_vaccine)
    return Response(serializer.data)

@api_view(['GET'])
def nearest_vaccine(request, pk):
    try:
        child_instance = Child.objects.get(id=pk)
    except Child.DoesNotExist:
        return Response({"error": "Child with this ID does not exist"}, status=404)
    
    nearest_vaccine = Vaccin.objects.nearest_vaccine_for_child(child_instance)
    serializer = VaccinSerializers(nearest_vaccine)
    
    # List of fields to include in the response
    fields_to_include = ['name', 'decsription','ageindays']
    
    # Filter serializer data for the desired fields
    filtered_data = {key: serializer.data.get(key) for key in fields_to_include}
    
    return Response(filtered_data)
