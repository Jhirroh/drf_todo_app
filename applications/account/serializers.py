from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class SignupSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=50, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password', 'email')

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords did not match")
        return data


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
