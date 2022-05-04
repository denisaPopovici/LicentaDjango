from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token
from Licenta.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/new-post', add_post),
    path('api/new-rating/user/<str:userID>/location/<str:locationID>/rate/<str:rating>', add_rating),
    path('admin/', admin.site.urls),
    path('api/', include('Licenta.urls')),
    path('api/posts', get_all_posts),
    path('api/recommendations/<str:userID>', get_recommended_locations_for_user),
    path('api/all-users-except/<str:id>', get_all_users_except_one),
    path('api/user/<str:userID>/feed-posts', feed_posts),
    path('api/user/<str:userID>/posts', get_all_user_posts),
    path('api/comments', get_all_comments),
    path('api/delete-comment/<str:commentID>', delete_comment),
    path('auth/', obtain_auth_token),
    path('api/locations', get_all_locations),
    path('api/random-locations/<str:userID>', get_random_locations),
    path('api/<str:token>', get_user_by_token),
    path('api/location/<str:locationName>', get_location_by_name),
    path('api/location-by-id/<str:locationID>', get_location_by_id),
    path('api/user/<str:username>', get_user_by_username),
    path('api/notification/<str:type>/to/<str:notified>/from/<notifying>/post/<str:postID>/comment/<str:commentID>', add_notification),
    path('api/user/<str:userID>/followers', get_all_followers),
    path('api/user/<str:userID>/notifications', get_all_notifications_for_user),
    path('api/does-user/<str:followerID>/follow/<str:followedID>', does_user_follow_user),
    path('api/user/<str:followerID>/follows/<str:followedID>', follow),
    path('api/user/<str:followerID>/unfollows/<str:followedID>', unfollow),
    path('api/read-notification/<str:notificationID>', read_notification),
    path('api/user/<str:userID>/visited-locations', get_all_visited_locations),
    path('api/user/<str:userID>/visited-locations-dropdown', get_all_visited_locations_for_dropdown),
    path('api/user/<str:userID>/image', change_user_image),
    path('api/user/<str:userID>/about', change_about),
    path('api/user/<str:userID>/add-xp/<str:xp>', add_xp),
    path('api/user/<str:userID>/visited-location/<str:locationID>', add_visited_location),
    path('api/user/<str:userID>/first-name', change_first_name),
    path('api/user/<str:userID>/last-name', change_last_name),
    path('api/user/<str:userID>/username', change_username),
    path('api/level/<str:levelNo>', get_level_by_number),
    path('api/user/<str:userID>/email', change_email),
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
