from django.urls import path  
from . import views
urlpatterns = [
    path('', views.getUsers),
    path('create/',views.SignUpView.as_view(), name ='create'),
    
]