from django.urls import path
from . import views
urlpatterns = [
    path('profiles/', views.profile_list_create),
    path('profiles/<int:pk>/', views.profile_detail_update),
    path('profiles/<int:pk>/delete/', views.profile_delete),
    path('profiles/create/', views.profile_create),
]
