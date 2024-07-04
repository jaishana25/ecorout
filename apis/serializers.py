from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
        
class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trips
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        Profile.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    username = models.CharField()
    password = models.CharField()