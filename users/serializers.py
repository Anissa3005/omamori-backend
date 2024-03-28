from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True},
                        'username': {'write_only': True}}

    # Make sure that the password is salted and hashed before when .saving() is called
    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
