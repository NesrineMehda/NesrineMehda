from django.urls import path 
from . import views
urlpatterns = [
 path('hokmatli',views.Fever_instance.as_view(),name ="fever"),
 path('',views.fever),

]