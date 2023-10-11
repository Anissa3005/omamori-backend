from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    uuid = models.UUIDField(editable=False)
    shrine_name = models.CharField(max_length=200)
    location = ArrayField(models.DecimalField(
        max_digits=9, decimal_places=6), size=2)
    description = models.CharField(max_length=300, blank=True)
    omamori_picture = models.FileField(upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
