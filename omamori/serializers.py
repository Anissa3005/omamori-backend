from rest_framework import serializers
from .models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'uuid', 'omamori_picture', 'shrine_name', 'location']
