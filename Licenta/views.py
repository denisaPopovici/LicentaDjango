import os
import random
from random import sample
import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
from rest_framework import viewsets
from django.contrib.auth.models import User

from LicentaDjango import settings
from .serializers import UserSerializer, LocationSerializer, CustomUserSerializer, PostSerializerGet, CommentSerializer, \
    UserSerializerUpload, UserLikePostSerializer, UserFollowSerializer, VisitedLocationsSerializer, \
    NotificationSerializer, VisitedLocationsSerializerForDropDown, PostSerializerUpload, LevelSerializer, \
    RatingSerializer
from Licenta.models import *
from django.http import JsonResponse, QueryDict
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
import pandas as pd


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
    if request.method == "GET":
        try:
            list = Location.objects.all()
            locationSerializer = LocationSerializer(list, many=True)
            return JsonResponse(locationSerializer.data, safe=False, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return JsonResponse([], safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
# @authentication_classes([TokenAuthentication, ])
# @permission_classes([IsAuthenticated, ])
def get_random_locations(request, userID):
    if request.method == "GET":
        try:
            list = Location.objects.all()
            user = CustomUser.objects.get(id=userID)
            not_visited = []
            for item in list:
                try:
                    visited = VisitedLocations.objects.get(location=item, user=user)
                except:  # it was not visited
                    not_visited.append(item)
            random_list = sample(not_visited, k=3)
            print(random_list)
            locationSerializer = LocationSerializer(random_list, many=True)
            return JsonResponse(locationSerializer.data, safe=False, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return JsonResponse([], safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
# @authentication_classes([TokenAuthentication, ])
# @permission_classes([IsAuthenticated, ])
def get_all_notifications_for_user(request, userID):
    if request.method == "GET":
        try:
            custom_user = CustomUser.objects.get(id=userID)
            print(custom_user)
            list = Notification.objects.filter(notified=custom_user)
            print(list)
            notificationSerializer = NotificationSerializer(list, many=True)
            return JsonResponse(notificationSerializer.data, safe=False, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return JsonResponse([], safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
# @authentication_classes([TokenAuthentication, ])
# @permission_classes([IsAuthenticated, ])
def get_all_posts(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        post_serializer = PostSerializerGet(posts, many=True)
        return JsonResponse(post_serializer.data, safe=False)


@api_view(['GET'])
# @authentication_classes([TokenAuthentication, ])
# @permission_classes([IsAuthenticated, ])
def get_all_users_except_one(request, id):
    if request.method == 'GET':
        users = CustomUser.objects.exclude(id=id)
        print(users)
        user_serializer = CustomUserSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)


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
def get_location_by_name(request, locationName):
    if (request.method == "GET"):
        try:
            location = Location.objects.get(name=locationName)
            locationSerializer = LocationSerializer(location)
            return JsonResponse(locationSerializer.data, safe=False, status=status.HTTP_200_OK)
        except Exception:
            return JsonResponse([], safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
# @authentication_classes([TokenAuthentication, ])
# @permission_classes([IsAuthenticated, ])
def get_location_by_id(request, locationID):
    print("hereee")
    if request.method == "GET":
        try:
            print("ere")
            location = Location.objects.get(id=locationID)
            print(location)
            locationSerializer = LocationSerializer(location)
            print(locationSerializer.data)
            return JsonResponse(locationSerializer.data, safe=False, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return JsonResponse([], safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
# @authentication_classes([TokenAuthentication, ])
# @permission_classes([IsAuthenticated, ])
def get_level_by_number(request, levelNo):
    if (request.method == "GET"):
        try:
            print(levelNo)
            level = Level.objects.get(id=levelNo)
            print(level)
            levelSerializer = LevelSerializer(level)
            print(levelSerializer.data)
            return JsonResponse(levelSerializer.data, safe=False, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
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
            custom_user = CustomUser.objects.get(id=userID)
            liked = UserLikePost.objects.filter(user=custom_user)
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
# @authentication_classes([TokenAuthentication, ])
# @permission_classes([IsAuthenticated, ])
def get_all_followers(request, userID):
    if request.method == "GET":
        followers = UserFollow.objects.filter(followed=userID)
        userFollowSerializer = UserFollowSerializer(followers, many=True)
        return JsonResponse(userFollowSerializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
# @authentication_classes([TokenAuthentication, ])
# @permission_classes([IsAuthenticated, ])
def does_user_follow_user(request, followerID, followedID):
    if request.method == "GET":
        follows = UserFollow.objects.filter(followed=followedID, follower=followerID)
        print(follows)
        userFollowSerializer = UserFollowSerializer(follows, many=True)
        return JsonResponse(userFollowSerializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
# @authentication_classes([TokenAuthentication, ])
# @permission_classes([IsAuthenticated, ])
def get_all_visited_locations(request, userID):
    if request.method == "GET":
        locations = VisitedLocations.objects.filter(user=userID)
        visitedLocationsSerializer = VisitedLocationsSerializer(locations, many=True)
        return JsonResponse(visitedLocationsSerializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
# @authentication_classes([TokenAuthentication, ])
# @permission_classes([IsAuthenticated, ])
def get_all_visited_locations_for_dropdown(request, userID):
    if request.method == "GET":
        locations = VisitedLocations.objects.filter(user=userID)
        visitedLocationsSerializer = VisitedLocationsSerializerForDropDown(locations, many=True)
        return JsonResponse(visitedLocationsSerializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_visited_location(request, userID, locationID):
    if (request.method == 'POST'):
        try:
            user = CustomUser.objects.get(id=userID)
            location = Location.objects.get(id=locationID)
            visited = VisitedLocations.objects.create(user=user, location=location)
            visited.save()
            serializer = VisitedLocationsSerializer(visited)
            return JsonResponse(serializer.data)
        except Exception:
            return JsonResponse([], safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
# @authentication_classes([TokenAuthentication, ])
# @permission_classes([IsAuthenticated, ])
def get_all_user_posts(request, userID):
    if request.method == "GET":
        posts = Post.objects.filter(user=userID)
        postSerializer = PostSerializerGet(posts, many=True)
        return JsonResponse(postSerializer.data, safe=False, status=status.HTTP_200_OK)


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
        custom_user_data['level'] = custom_user.level
        print(request.FILES)
        serializer_upload = UserSerializerUpload(custom_user_data, request.FILES, instance=custom_user)
        if serializer_upload.is_valid():
            print("IS VALID")
            image_path = old_picture.path
            print(image_path)
            if os.path.exists(image_path):
                os.remove(image_path)
            serializer_upload.save()
            serializer = CustomUserSerializer(custom_user)
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse({'message': 'The image was not uploaded'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def change_about(request, userID):
    if request.method == 'PUT':
        custom_user = CustomUser.objects.get(id=userID)
        custom_user.about = request.data['about']
        try:
            custom_user.save(update_fields=['about'])
        except Exception as e:
            print(e)

        print(custom_user.about)
        return JsonResponse({'message': 'About saved'}, status=status.HTTP_200_OK)


@api_view(['PUT'])
def add_xp(request, userID, xp):
    if request.method == 'PUT':
        custom_user = CustomUser.objects.get(id=userID)
        custom_user.xp = custom_user.xp + int(xp)
        try:
            custom_user.save(update_fields=['xp'])
        except Exception as e:
            print(e)
        print(custom_user.xp)
        return JsonResponse({'message': 'XP saved'}, status=status.HTTP_200_OK)


@api_view(['PUT'])
def change_username(request, userID):
    if request.method == 'PUT':
        try:
            custom_user = CustomUser.objects.get(id=userID)
            user_id = custom_user.user_id
            user = User.objects.get(id=user_id)
            user.username = request.data['username']
            user.save()
            custom_user.username = request.data['username']
            custom_user.save()
            return JsonResponse({'message': 'Username saved'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)


@api_view(['PUT'])
def change_first_name(request, userID):
    if request.method == 'PUT':
        try:
            custom_user = CustomUser.objects.get(id=userID)
            user_id = custom_user.user_id
            user = User.objects.get(id=user_id)
            user.first_name = request.data['first_name']
            user.save()
            custom_user.first_name = request.data['first_name']
            custom_user.save()
            return JsonResponse({'message': 'First name saved'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)


@api_view(['PUT'])
def change_last_name(request, userID):
    if request.method == 'PUT':
        try:
            custom_user = CustomUser.objects.get(id=userID)
            user_id = custom_user.user_id
            user = User.objects.get(id=user_id)
            user.last_name = request.data['last_name']
            user.save()
            custom_user.last_name = request.data['last_name']
            custom_user.save()
            return JsonResponse({'message': 'Last name saved'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)


@api_view(['PUT'])
def change_email(request, userID):
    if request.method == 'PUT':
        custom_user = CustomUser.objects.get(id=userID)
        user_id = custom_user.user_id
        user = User.objects.get(id=user_id)
        user.email = request.data['email']
        user.save()
        custom_user.email = request.data['email']
        custom_user.save()
        return JsonResponse({'message': 'Email saved'}, status=status.HTTP_200_OK)


@api_view(['PUT'])
def read_notification(request, notificationID):
    if request.method == 'PUT':
        notification = Notification.objects.get(id=notificationID)
        notification.read = True
        notification.save()
        return JsonResponse({'message': 'Notification saved'}, status=status.HTTP_200_OK)


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
            # remove like
            post.no_likes -= 1
            post.save()
            postUserLike.delete()
            post_serializer = PostSerializerGet(post)
            return JsonResponse(post_serializer.data)
        except UserLikePost.DoesNotExist:  # like
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
        data = request.data  # the text of the comment
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

@api_view(['POST'])
def add_rating(request, userID, locationID, rating):
    if (request.method == 'POST'):
        try:
            user = CustomUser.objects.get(id=userID)
            location = Location.objects.get(id=locationID)
            ratingObj = Rating.objects.create(user = user, location = location, rating = rating)
            ratingObj.save()
            rating_serializer = RatingSerializer(ratingObj)
            return JsonResponse(rating_serializer.data)
        except Exception:
            return JsonResponse([], safe=False, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_notification(request, type, notified, notifying, postID, commentID):
    if (request.method == 'POST'):
        try:
            notified_user = CustomUser.objects.get(id=notified)
            notifying_user = CustomUser.objects.get(id=notifying)
            if postID != '0':
                post = Post.objects.get(id=postID)
            else:
                post = None
            if commentID == '0':
                comment = None
            else:
                comment = Comment.objects.get(id=commentID)
            notification = Notification.objects.create(type=type, notified=notified_user, notifying=notifying_user,
                                                       post=post, comment=comment)
            notification.save()
            notification_serializer = NotificationSerializer(notification)
            return JsonResponse(notification_serializer.data)
        except Exception as e:
            print(e)
            return JsonResponse([], safe=False, status=status.HTTP_200_OK)


@api_view(['POST'])
def follow(request, followerID, followedID):
    if (request.method == 'POST'):
        try:
            follower = CustomUser.objects.get(id=followerID)
            followed = CustomUser.objects.get(id=followedID)
            userFollow = UserFollow.objects.create(follower=follower, followed=followed)
            userFollow.save()
            userFollowSerializer = UserFollowSerializer(userFollow)
            return JsonResponse(userFollowSerializer.data)
        except Exception:
            return JsonResponse([], safe=False, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def unfollow(request, followerID, followedID):
    if (request.method == 'DELETE'):
        try:
            follower = CustomUser.objects.get(id=followerID)
            followed = CustomUser.objects.get(id=followedID)
            userFollow = UserFollow.objects.get(follower=follower, followed=followed)
            if userFollow:
                userFollow.delete()
            return JsonResponse({'message': 'Unfollowed successfully'})
        except Exception:
            return JsonResponse([], safe=False, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_comment(request, commentID):
    if request.method == 'DELETE':
        try:
            comment = Comment.objects.get(id=commentID)
            if comment:
                comment.delete()
            return JsonResponse({'message': 'Deleted successfully'})
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
        followed_users = UserFollow.objects.filter(follower=user, )
        posts = []
        for followed_user in followed_users:
            posts.extend(Post.objects.filter(user=followed_user.followed))

        new = []
        for i in posts:  # remove duplicates
            if i not in new:
                new.append(i)

        post_serializer = PostSerializerGet(new, many=True)
        return JsonResponse(post_serializer.data, safe=False)


@api_view(['POST'])
def add_post(request):
    print("hereee")
    if request.method == 'POST':
        data = request.data
        postSerializer = PostSerializerUpload(data=request.data)
        if postSerializer.is_valid():
            post = postSerializer.save()
            newPost = PostSerializerGet(Post.objects.get(pk=post.id))
            return JsonResponse(newPost.data, status=status.HTTP_200_OK)
        else:
            print(postSerializer.errors)
            return JsonResponse({'message': postSerializer.errors}, status=status.HTTP_400_BAD_REQUEST)


def getRating(user_id, location_id):
    rating = Rating.objects.filter(user_id=user_id, location_id=location_id)
    if not rating:
        return 0
    else:
        return rating[0].rating


def standardize(row):
    new_row = (row - row.mean()) / (row.max() - row.min())
    return new_row


def get_recommended_locations(item_similarity_df, location_id, user_rating):
    # we substract 2.5 so that when the rating is low (under 2.5), we make the score/similarity negative so that we
    # do not recommend locations that are similar to this one
    similar_score = item_similarity_df[location_id] * (user_rating - 2.5)
    similar_score = similar_score.sort_values(ascending=False)  # from best to worst
    return similar_score  # similar score represents the percentage in which the movies should be recommended to us


def get_recommendations(self, userID):
    locations = Location.objects.all()
    users = CustomUser.objects.all()
    user_ids = list()
    location_ids = list()
    for item in users:
        user_ids.append(item.id)
    for item in locations:
        location_ids.append(item.id)

    df = pd.DataFrame(index=user_ids, columns=location_ids)
    for user_id in user_ids:
        for location_id in location_ids:
            df.at[user_id, location_id] = getRating(user_id, location_id)

    ratings_std = df.apply(standardize, axis=1)
    # we are taking the transpose since we want the similarity between items (cosine_similarity works on the rows but
    # our items are on the columns)
    item_similarity = cosine_similarity(ratings_std.T)  # we obtain the similarity matrix

    item_similarity_df = pd.DataFrame(item_similarity, index=df.columns, columns=df.columns)

    my_user = CustomUser.objects.get(id=userID)
    ratings = Rating.objects.filter(user=my_user)
    rating_list = list()
    location_ids = list()
    for item in ratings:
        location_ids.append(item.location.id)
        rating_list.append(item.rating)
    my_list = list(zip(location_ids, rating_list))

    recommended_locations = pd.DataFrame()
    for location, rating in my_list:
        # for every rating we will obtain a row with the recommended locations based on that rating
        result = pd.DataFrame(get_recommended_locations(item_similarity_df, location, rating))
        recommended_locations = pd.concat([recommended_locations, result.T])

    # for every row/rating, we sum the scores obtained for each movie, which represent the percentage in which that
    # movie should be recommended, the movie with the highest score is first
    return recommended_locations.sum().sort_values(ascending=False)


@api_view(['GET'])
def get_recommended_locations_for_user(self, userID):
    try:
        user = CustomUser.objects.get(id=userID)
        result = get_recommendations(self, userID)
        locations = []
        for item in result.index.values:
            location = Location.objects.get(id=item)
            try:
                visited = VisitedLocations.objects.get(location=location, user=user)
            except:  # it was not visited
                locations.append(location)
                print("already visited")
        locationSerializer = LocationSerializer(locations[:3], many=True)
        return JsonResponse(locationSerializer.data, safe=False, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return JsonResponse([], safe=False, status=status.HTTP_200_OK)
