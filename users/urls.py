from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path('newuser/', views.create_user, name='create_users'),
]
