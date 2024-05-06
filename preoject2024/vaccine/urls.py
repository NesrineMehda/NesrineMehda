from django.urls import path  
from . import views
urlpatterns = [
path('<str:pk>/',views.nearest_vaccine__all,name='nearest'),
path('<str:pk>/nearest/',views.nearest_vaccine,name='nearest vaccin'),


]