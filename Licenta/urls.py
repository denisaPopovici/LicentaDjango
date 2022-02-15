from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import UserViewSet, CustomUserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('custom-users', CustomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]