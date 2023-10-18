from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid


class Users(models.Model):
    username = models.CharField(max_length=30)
    uuid = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Omamori(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    shrine_name = models.CharField(max_length=20)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.CharField(max_length=300, blank=True)
    omamori_picture = models.FileField(upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
