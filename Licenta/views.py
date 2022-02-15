from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, LocationSerializer, CustomUserSerializer
from Licenta.models import *
from django.http import JsonResponse
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
    if (request.method == "GET"):
        try:
            list = Location.objects.all()
            groupSerializer = LocationSerializer(list, many=True)
            return JsonResponse(groupSerializer.data, safe=False, status=status.HTTP_200_OK)
        except Exception:
            return JsonResponse([], safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
# @authentication_classes([TokenAuthentication, ])
# @permission_classes([IsAuthenticated, ])
def get_user_by_username(request, username):
    if (request.method == "GET"):
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
def get_user_by_token(request, token):
    if (request.method == "GET"):
        try:
            found = Token.objects.get(key=token).user
            userSerializer = UserSerializer(found)
            return JsonResponse(userSerializer.data, safe=False, status=status.HTTP_200_OK)
        except Exception:
            return JsonResponse([], safe=False, status=status.HTTP_200_OK)
