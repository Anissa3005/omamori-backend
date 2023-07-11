from rest_framework import serializers
from .models import Users
from .models import Omamori


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username', 'email', 'created_at', 'updated_at']


class OmamoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Omamori
        fields = ['id', 'users_id', 'shrine_name', 'location', 'description']
