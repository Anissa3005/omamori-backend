from rest_framework import serializers
from .models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'uuid', 'omamori_picture',
                  'shrine_name', 'longitude', 'latitude']
