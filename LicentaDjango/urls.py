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
    path('api/posts', get_all_posts),
    path('api/user/<str:userID>/feed-posts', feed_posts),
    path('api/comments', get_all_comments),
    path('auth/', obtain_auth_token),
    path('api/locations', get_all_locations),
    path('api/<str:token>', get_user_by_token),
    path('api/user/<str:username>', get_user_by_username),
    path('api/user-by-id/<str:userID>', change_user_image),
    path('api/custom-user/<str:username>', get_custom_user_by_username),
    path('api/posts/<str:postID>/users/<str:userID>/like-post', like_post),
    path('api/user/<str:userID>/liked-posts', all_posts_user_likes),
    path('api/posts/<str:postID>/users/<str:userID>/comment-post', add_comment),
    path('api/user/<str:userID>/post/<str:postID>/did-like', did_user_like_post),
    path('api/user/<str:userID>/get-by-id', get_custom_user_by_id),
    path('api/get-comments-to-post/<str:postID>', get_all_comments_to_post),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
