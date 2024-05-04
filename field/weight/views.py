from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CalculateBMISerializer

class CalculateBMIView(APIView):
    def post(self, request):
        serializer = CalculateBMISerializer(data=request.data)
        if serializer.is_valid():
            age = serializer.validated_data['age']
            weight = serializer.validated_data['weight']
            height = serializer.validated_data['height']

            # Perform BMI calculation logic here
            bmi = weight / (height * height)

            # Determine BMI category based on age-specific criteria
            bmi_category = self.get_bmi_category(age, bmi)

            return Response({'bmi': bmi, 'bmi_category': bmi_category}, status=200)
        else:
            return Response(serializer.errors, status=400)

    def get_bmi_category(self, age, bmi):
        if age < 2:
            # BMI categories for children under 2 years old
            if bmi < 16:
                return 'Underweight'
            elif bmi < 18:
                return 'Normal weight'
            elif bmi < 20:
                return 'Overweight'
            else:
                return 'Obese'
        else:
            # BMI categories for children aged 2 to 6 years old
            if bmi < 15:
                return 'Underweight'
            elif bmi < 18.5:
                return 'Normal weight'
            elif bmi < 25:
                return 'Overweight'
            else:
                return 'Obese'
