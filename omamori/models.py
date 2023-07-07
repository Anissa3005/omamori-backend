from django.db import models
from django.contrib.postgres.fields import ArrayField


class Users(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Omamori(models.Model):
    users_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    shrine_name = models.CharField(max_length=200)
    location = ArrayField(models.DecimalField(
        max_digits=9, decimal_places=6), size=2)
    description = models.CharField(max_length=300, blank=True)
