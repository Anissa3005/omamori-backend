from rest_framework import serializers
from .models import Users, Omamori
import re


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'uuid']

    def validate_username(self, value):
        regex_special_characters = r"[~`!#$%\^&*+={}()\-\[\]\\']+"
        regex_non_latin = r"[^\u0000-\u007F]+"
        contains_invalid_character = re.search(regex_special_characters, value)
        contains_invalid_alphabet = re.search(regex_non_latin, value)

        if contains_invalid_character != None:
            raise serializers.ValidationError('INVALID_CHARACTERS')

        if contains_invalid_alphabet != None:
            raise serializers.ValidationError('CONTAINS_NON_LATIN_CHARACTERS')

        if len(value.replace(" ", "")) <= 1:
            raise serializers.ValidationError('INVALID_LENGTH')
        return value


class OmamoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Omamori
        fields = ['user', 'shrine_name', 'longitude',
                  'latitude', 'description', 'omamori_picture']
