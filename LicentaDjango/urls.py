from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token
from Licenta.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Licenta.urls')),
    path('auth/', obtain_auth_token),
    path('api/locations', get_all_locations),
    path('api/<str:token>', get_user_by_token),
    path('api/user/<str:username>', get_user_by_username),
    path('api/custom-user/<str:username>', get_custom_user_by_username),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
