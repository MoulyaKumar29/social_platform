from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from posts.models import Post


from .models import Follow, FriendRequest, Notification


@login_required
def send_friend_request(request, username):
    receiver = get_object_or_404(User, username=username)

    if receiver != request.user:
        FriendRequest.objects.get_or_create(
            sender=request.user,
            receiver=receiver
        )

    return redirect("friend_list")


@login_required
def friend_list(request):
    received_requests = FriendRequest.objects.filter(
        receiver=request.user,
        accepted=False
    )

    sent_requests = FriendRequest.objects.filter(
        sender=request.user,
        accepted=False
    )

    accepted_received = FriendRequest.objects.filter(
        receiver=request.user,
        accepted=True
    )

    accepted_sent = FriendRequest.objects.filter(
        sender=request.user,
        accepted=True
    )

    return render(
        request,
        "friends/friend_list.html",
        {
            "received_requests": received_requests,
            "sent_requests": sent_requests,
            "accepted_received": accepted_received,
            "accepted_sent": accepted_sent,
        }
    )


@login_required
def accept_friend_request(request, request_id):
    friend_request = get_object_or_404(
        FriendRequest,
        id=request_id,
        receiver=request.user
    )

    friend_request.accepted = True
    friend_request.save()

    Notification.objects.create(
        recipient=friend_request.sender,
        sender=request.user,
        notification_type="friend_request_accepted",
        message=f"{request.user.username} accepted your friend request."
    )

    return redirect("friend_list")


@login_required
def reject_friend_request(request, request_id):
    friend_request = get_object_or_404(
        FriendRequest,
        id=request_id,
        receiver=request.user
    )

    friend_request.delete()

    return redirect("friend_list")

@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)

    if user_to_follow != request.user:
        Follow.objects.get_or_create(
            follower=request.user,
            following=user_to_follow
        )

    return redirect("user_list")


@login_required
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(User, username=username)

    Follow.objects.filter(
        follower=request.user,
        following=user_to_unfollow
    ).delete()

    return redirect("user_list")

@login_required
def user_list(request):
    search_query = request.GET.get("search", "")

    users = User.objects.exclude(id=request.user.id)

    if search_query:
        users = users.filter(
            username__icontains=search_query
        )

    following_ids = Follow.objects.filter(
        follower=request.user
    ).values_list("following_id", flat=True)

    return render(
        request,
        "friends/user_list.html",
        {
            "users": users,
            "following_ids": following_ids,
            "search_query": search_query,
        }
    )

@login_required
def following_list(request):
    following = Follow.objects.filter(
        follower=request.user
    ).select_related("following")

    return render(
        request,
        "friends/following.html",
        {"following": following}
    )


@login_required
def followers_list(request):
    followers = Follow.objects.filter(
        following=request.user
    ).select_related("follower")

    return render(
        request,
        "friends/followers.html",
        {"followers": followers}
    )

@login_required
def notification_list(request):
    notifications = request.user.notifications.all()

    return render(
        request,
        "friends/notifications.html",
        {"notifications": notifications}
    )

@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)

    if user_to_follow != request.user:
        follow, created = Follow.objects.get_or_create(
            follower=request.user,
            following=user_to_follow
        )

        if created:
            Notification.objects.create(
                recipient=user_to_follow,
                sender=request.user,
                notification_type="follow",
                message=f"{request.user.username} started following you."
            )

    return redirect("user_list")

@login_required
def send_friend_request(request, username):
    receiver = get_object_or_404(User, username=username)

    if receiver != request.user:
        friend_request, created = FriendRequest.objects.get_or_create(
            sender=request.user,
            receiver=receiver
        )

        if created:
            Notification.objects.create(
                recipient=receiver,
                sender=request.user,
                notification_type="friend_request",
                message=f"{request.user.username} sent you a friend request."
            )

    return redirect("friend_list")

@login_required
def user_profile(request, username):
    profile_user = get_object_or_404(
        User,
        username=username
    )

    posts = Post.objects.filter(
        author=profile_user
    )

    is_following = Follow.objects.filter(
        follower=request.user,
        following=profile_user
    ).exists()

    existing_request = FriendRequest.objects.filter(
        sender=request.user,
        receiver=profile_user,
        accepted=False
    ).exists()

    return render(
        request,
        "friends/user_profile.html",
        {
            "profile_user": profile_user,
            "posts": posts,
            "is_following": is_following,
            "existing_request": existing_request,
        }
    )

