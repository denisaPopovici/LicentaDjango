import os

from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, LocationSerializer, CustomUserSerializer, PostSerializerGet, CommentSerializer, \
    UserSerializerUpload, UserLikePostSerializer
from Licenta.models import *
from django.http import JsonResponse, QueryDict
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

@api_view(['GET'])
# @authentication_classes([TokenAuthentication, ])
# @permission_classes([IsAuthenticated, ])
def get_all_locations(request):
    print("here")
    if request.method == "GET":
        try:
            list = Location.objects.all()
            locationSerializer = LocationSerializer(list, many=True)
            return JsonResponse(locationSerializer.data, safe=False, status=status.HTTP_200_OK)
        except Exception:
            return JsonResponse([], safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
# @authentication_classes([TokenAuthentication, ])
# @permission_classes([IsAuthenticated, ])
def get_all_posts(request):
    print("here")
    if request.method == 'GET':
        posts = Post.objects.all()
        post_serializer = PostSerializerGet(posts, many=True)
        return JsonResponse(post_serializer.data, safe=False)


@api_view(['GET'])
# @authentication_classes([TokenAuthentication, ])
# @permission_classes([IsAuthenticated, ])
def get_user_by_username(request, username):
    if request.method == "GET":
        try:
            user = User.objects.get(username=username)
            userSerializer = UserSerializer(user)
            return JsonResponse(userSerializer.data, safe=False, status=status.HTTP_200_OK)
        except Exception:
            return JsonResponse([], safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
# @authentication_classes([TokenAuthentication, ])
# @permission_classes([IsAuthenticated, ])
def get_custom_user_by_username(request, username):
    if (request.method == "GET"):
        try:
            user = User.objects.get(username=username)
            custom_user = CustomUser.objects.get(user=user)
            userSerializer = CustomUserSerializer(custom_user)
            return JsonResponse(userSerializer.data, safe=False, status=status.HTTP_200_OK)
        except Exception:
            return JsonResponse([], safe=False, status=status.HTTP_200_OK)

@api_view(['GET'])
# @authentication_classes([TokenAuthentication, ])
# @permission_classes([IsAuthenticated, ])
def get_custom_user_by_id(request, userID):
    if (request.method == "GET"):
        try:
            custom_user = CustomUser.objects.get(id=userID)
            userSerializer = CustomUserSerializer(custom_user)
            return JsonResponse(userSerializer.data, safe=False, status=status.HTTP_200_OK)
        except Exception:
            return JsonResponse([], safe=False, status=status.HTTP_200_OK)

@api_view(['GET'])
# @authentication_classes([TokenAuthentication, ])
# @permission_classes([IsAuthenticated, ])
def did_user_like_post(request, userID, postID):
    if (request.method == "GET"):
        try:
            liked = UserLikePost.objects.get(user=userID, post=postID)
            likedSerializer = UserLikePostSerializer(liked)
            return JsonResponse(likedSerializer.data, safe=False, status=status.HTTP_200_OK)
        except Exception:
            return JsonResponse([], safe=False, status=status.HTTP_200_OK)

@api_view(['GET'])
# @authentication_classes([TokenAuthentication, ])
# @permission_classes([IsAuthenticated, ])
def all_posts_user_likes(request, userID):
    if request.method == "GET":
        try:
            print("here")
            custom_user = CustomUser.objects.get(id=userID)
            print(custom_user)
            liked = UserLikePost.objects.filter(user=custom_user)
            print(liked)
            likedSerializer = UserLikePostSerializer(liked, many=True)
            return JsonResponse(likedSerializer.data, safe=False, status=status.HTTP_200_OK)
        except Exception:
            return JsonResponse([], safe=False, status=status.HTTP_200_OK)

@api_view(['GET'])
# @authentication_classes([TokenAuthentication, ])
# @permission_classes([IsAuthenticated, ])
def get_all_comments_to_post(request, postID):
    if request.method == "GET":
        try:
            comment = Comment.objects.get(post=postID)
            commentSerializer = CommentSerializer(comment)
            return JsonResponse(commentSerializer.data, safe=False, status=status.HTTP_200_OK)
        except Exception:
            return JsonResponse([], safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
# @authentication_classes([TokenAuthentication, ])
# @permission_classes([IsAuthenticated, ])
def get_all_comments(request):
    if request.method == "GET":
        comments = Comment.objects.all()
        commentSerializer = CommentSerializer(comments, many=True)
        return JsonResponse(commentSerializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user_by_token(request, token):
    if request.method == "GET":
        try:
            found = Token.objects.get(key=token).user
            userSerializer = UserSerializer(found)
            return JsonResponse(userSerializer.data, safe=False, status=status.HTTP_200_OK)
        except Exception:
            return JsonResponse([], safe=False, status=status.HTTP_200_OK)


@api_view(['PUT'])
# @authentication_classes([TokenAuthentication, ])
# @permission_classes([IsAuthenticated, ])
def change_user_image(request, userID):
    if request.method == 'PUT':
        custom_user = CustomUser.objects.get(id=userID)
        print(custom_user)
        old_picture = custom_user.image
        custom_user_data = QueryDict('', mutable=True)
        custom_user_data['user'] = custom_user.user
        custom_user_data['about'] = custom_user.about
        serializer_upload = UserSerializerUpload(custom_user_data, request.FILES, instance=custom_user)
        if serializer_upload.is_valid():
            image_path = old_picture.path
            if os.path.exists(image_path):
                os.remove(image_path)
            serializer_upload.save()
            serializer = UserSerializer(custom_user)
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse({'message': 'The image was not uploaded'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
# @authentication_classes([TokenAuthentication, ])
# @permission_classes([IsAuthenticated, ])
def like_post(request, postID, userID):
    if (request.method == 'POST'):
        print('here')
        try:
            user = CustomUser.objects.get(id=userID)
            print(user)
            post = Post.objects.get(id=postID)
            print(post)
            postUserLike = UserLikePost.objects.get(user=user, post=post)
            print(postUserLike)
            #remove like
            post.no_likes -= 1
            post.save()
            postUserLike.delete()
            post_serializer = PostSerializerGet(post)
            return JsonResponse(post_serializer.data)
        except UserLikePost.DoesNotExist: #like
            print('here')
            post.no_likes += 1
            post.save()
            print('here')
            postUserLike = UserLikePost.objects.create(post=post, user=user)
            print('here')
            postUserLike.save()
            print('here')
            post_serializer = PostSerializerGet(post)
            return JsonResponse(post_serializer.data)

@api_view(['POST'])
def add_comment(request, postID, userID):
    if (request.method == 'POST'):
        data = request.data #the text of the comment
        try:
            user = CustomUser.objects.get(id=userID)
            print(user)
            post = Post.objects.get(id=postID)
            print(post)
            print(data)
            comment = Comment.objects.create(post=post, user=user, text=data)
            print('here')
            comment.save()
            print('here')
            comment_serializer = CommentSerializer(comment)
            return JsonResponse(comment_serializer.data)
        except Exception:
            return JsonResponse([], safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
def feed_posts(request, userID):
    """
    Retrieves all the posts posted by the users the current user follows
    """
    user = CustomUser.objects.get(id=userID)
    if request.method == 'GET':
        posts = Post.objects.all().order_by('date')
        followed_users = UserFollow.objects.filter(follower=user)
        posts = []
        for followed_user in followed_users:
            posts.extend(Post.objects.filter(user=followed_user.followed))

        post_serializer = PostSerializerGet(posts, many=True)
        return JsonResponse(post_serializer.data, safe=False)
