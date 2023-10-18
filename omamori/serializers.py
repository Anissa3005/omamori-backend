from rest_framework import serializers
from .models import Users, Omamori


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'uuid']


class OmamoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Omamori
        fields = ['user', 'shrine_name', 'longitude',
                  'latitude', 'description', 'omamori_picture']
