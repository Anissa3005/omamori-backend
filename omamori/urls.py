from django.contrib import admin
from django.urls import path
from omamori import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.users_list, name='user'),
    path('user/<str:uuid>/', views.user_by_uuid, name='user-by-uuid'),
    # path('omamori/', views.omamori_list, name='omamori')
]
