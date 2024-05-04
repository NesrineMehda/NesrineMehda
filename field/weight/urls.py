from django.urls import path
from .views import CalculateBMIView

urlpatterns = [
    path('calculate-bmi/', CalculateBMIView.as_view(), name='calculate_bmi'),
]
