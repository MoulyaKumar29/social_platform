from django.urls import path

from . import views


urlpatterns = [
    path("", views.friend_list, name="friend_list"),

    path(
        "send/<str:username>/",
        views.send_friend_request,
        name="send_friend_request"
    ),

    path(
        "accept/<int:request_id>/",
        views.accept_friend_request,
        name="accept_friend_request"
    ),

    path(
        "reject/<int:request_id>/",
        views.reject_friend_request,
        name="reject_friend_request"
    ),

    path(
        "follow/<str:username>/",
        views.follow_user,
        name="follow_user"
    ),

    path(
        "unfollow/<str:username>/",
        views.unfollow_user,
        name="unfollow_user"
    ),

    path("users/", views.user_list, name="user_list"),

    path(
    "following/",
    views.following_list,
    name="following_list"
    ),

    path(
        "followers/",
        views.followers_list,
        name="followers_list"
    ),

    path(
    "notifications/",
    views.notification_list,
    name="notifications"
    ),


    path(
    "profile/<str:username>/",
    views.user_profile,
    name="user_profile"
    ),
]