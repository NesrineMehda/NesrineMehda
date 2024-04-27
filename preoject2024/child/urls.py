from django.urls import path  
from . import views
urlpatterns = [
    path('',views.childs),
    path('add/',views.addchild),
    path('<str:pk>/update',views.updatechild),
    path( '<str:pk>/delete',views.deletechild),

]