from rest_framework import serializers
from .models import Users, Omamori
import re
from omamori.results import Error


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['uuid']

    def validate_uuid(self, value):
        if len(value.replace(" ", "")) <= 1:
            raise serializers.ValidationError(Error.INVALID_LENGTH)
        return value


class OmamoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Omamori
        fields = ['user', 'shrine_name', 'longitude',
                  'latitude', 'description', 'omamori_picture']

    def validate_shrine_name(self, value):
        regex_special_characters = r"[~`!#$%\^&*+={}()\-\[\]\\']+"
        contains_invalid_character = re.search(
            regex_special_characters, value)

        if contains_invalid_character != None:
            raise serializers.ValidationError(Error.INVALID_CHARACTERS)

        return value

    def validate_description(self, value):
        if len(value.replace(" ", "")) <= 1:
            raise serializers.ValidationError(Error.INVALID_LENGTH)

        return value

    def validate_longitude(self, value):
        if value == 0:
            raise serializers.ValidationError(Error.INVALID_LENGTH)

        return value

    def validate_latitude(self, value):
        if value == 0:
            raise serializers.ValidationError(Error.INVALID_LENGTH)

        return value
