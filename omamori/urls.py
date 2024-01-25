from django.contrib import admin
from django.urls import path
from omamori import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.users_list, name='users'),
    path('user/<str:uuid>/', views.user_by_uuid, name='user_by_uuid'),
    path('omamori/', views.omamori_list, name='omamori')
]
