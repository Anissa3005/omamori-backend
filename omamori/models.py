from django.db import models
from django.contrib.postgres.fields import ArrayField


class Users(models.Model):
    uuid = models.CharField(
        primary_key=True, unique=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Omamori(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    shrine_name = models.CharField(max_length=20)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.CharField(max_length=300, blank=True)
    omamori_picture = models.FileField(upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
