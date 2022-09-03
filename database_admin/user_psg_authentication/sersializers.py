from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserPSG


class UserPSGSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            password=make_password(validated_data['password']),
            is_staff=True
        )

    class Meta:
        model = User
        fields = ('email', 'username', 'password', )







