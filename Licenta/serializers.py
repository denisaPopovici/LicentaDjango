from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from Licenta.models import *
from django import forms


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']
        # hidden password
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        # hashing the password
        user = User.objects.create_user(**validated_data)
        # add authtoken for each created user
        Token.objects.create(user=user)
        return user


class UserSerializerUpload(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('id',
                  'user',
                  'about',
                  'image')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id',
                  'name',
                  'latitude',
                  'longitude',
                  'image',)


class CommentSerializer(serializers.ModelSerializer):
    id_post = serializers.IntegerField(source='post.id')
    username = serializers.CharField(source='user.user.username')
    profile_image = serializers.ImageField(source='user.image')


    class Meta:
        model = Comment
        fields = (
            "id",
            "post",
            "id_post",
            "text",
            "user",
            "username",
            "profile_image",
        )


class PostSerializerGet(serializers.ModelSerializer):
    username = serializers.CharField(source='user.user.username')
    profile_image = serializers.ImageField(source='user.image')
    location_name = serializers.CharField(source='location.name')

    class Meta:
        model = Post
        fields = (
            "id",
            "user",
            "username",
            "profile_image",
            "location",
            "location_name",
            "date",
            "image",
            "description",
            "no_likes",
            "no_comments",
        )


class UserLikePostSerializer(serializers.ModelSerializer):
    id_post = serializers.IntegerField(source='post.id')

    class Meta:
        model = UserLikePost
        fields = ('post',
                  'id_post',
                  'user')

class UserFollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollow
        fields = ('follower',
                  'followed')


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
