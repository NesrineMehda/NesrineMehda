from django.urls import path 
from . import views
urlpatterns = [
 path('<str:pk>/',views.fever_instance,name ="fever"),
 path('',views.fever),

]