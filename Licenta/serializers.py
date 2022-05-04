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
                  'level',
                  'image')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id',
                  'name',
                  'latitude',
                  'longitude',
                  'image',
                  'xp',
                  'description',)


class CommentSerializer(serializers.ModelSerializer):
    id_post = serializers.IntegerField(source='post.id')
    username = serializers.CharField(source='user.user.username')
    profile_image = serializers.ImageField(source='user.image')
    user_id = serializers.IntegerField(source='user.id')

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
            "user_id",
        )


class NotificationSerializer(serializers.ModelSerializer):
    post_image = serializers.ImageField(source='post.image', default='')
    notifying_image = serializers.ImageField(source='notifying.image')
    notifying_username = serializers.CharField(source='notifying.user.username')
    notifying_id = serializers.IntegerField(source='notifying.id')
    comment_text = serializers.CharField(source='comment.text', default='')

    class Meta:
        model = Notification
        fields = (
            "id",
            "type",
            "notified",
            "notifying",
            "post",
            "comment",
            "post_image",
            "notifying_image",
            "notifying_username",
            "notifying_id",
            "comment_text",
            "read",
        )


class PostSerializerGet(serializers.ModelSerializer):
    username = serializers.CharField(source='user.user.username')
    profile_image = serializers.ImageField(source='user.image')
    location_name = serializers.CharField(source='location.name')
    location_latitude = serializers.CharField(source='location.latitude')
    location_longitude = serializers.CharField(source='location.longitude')
    user_id = serializers.IntegerField(source='user.id')

    class Meta:
        model = Post
        fields = (
            "id",
            "user",
            "user_id",
            "username",
            "profile_image",
            "location",
            "location_name",
            "date",
            "image",
            "description",
            "no_likes",
            "no_comments",
            "location_latitude",
            "location_longitude",
        )


class PostSerializerUpload(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "user",
            "location",
            "date",
            "image",
            "description",
            "no_likes",
            "no_comments",
        )


class VisitedLocationsSerializer(serializers.ModelSerializer):
    location_name = serializers.CharField(source='location.name')

    class Meta:
        model = VisitedLocations
        fields = (
            "user",
            "location",
            "location_name",
        )


class VisitedLocationsSerializerForDropDown(serializers.ModelSerializer):
    label = serializers.CharField(source='location.name')
    value = serializers.CharField(source='location.name')

    class Meta:
        model = VisitedLocations
        fields = (
            "label",
            "value",
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


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('id',
                  'inferior_limit',
                  'superior_limit'
                  )


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id',
                  'location',
                  'user',
                  'rating',
                  )


class CustomUserSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id')
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    password = serializers.CharField(source='user.password')
    email = serializers.CharField(source='user.email')

    class Meta:
        model = CustomUser
        fields = ('id',
                  'user_id',
                  'username',
                  'password',
                  'email',
                  'first_name',
                  'last_name',
                  'about',
                  'image',
                  'level',
                  'xp',
                  )

    def create(self, validated_data):
        # hashing the password
        user = CustomUser.objects.create_user(**validated_data)
        # add authtoken for each created user
        Token.objects.create(user=user)
        return user
