from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from Licenta.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']
        #hidden password
        extra_kwargs = {'password': {'write_only':True, 'required':True}}

    def create(self, validated_data):
        #hashing the password
        user = User.objects.create_user(**validated_data)
        #add authtoken for each created user
        Token.objects.create(user=user)
        return user

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id',
                  'name',
                  'latitude',
                  'longitude',
                  'image',)


class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    password = serializers.CharField(source='user.password')
    email = serializers.CharField(source='user.email')
    class Meta:
        model = CustomUser
        fields = ('id',
                  'username',
                  'password',
                  'email',
                  'first_name',
                  'last_name',
                  'about',
                  'image')

    def create(self, validated_data):
        # hashing the password
        user = CustomUser.objects.create_user(**validated_data)
        # add authtoken for each created user
        Token.objects.create(user=user)
        return user
