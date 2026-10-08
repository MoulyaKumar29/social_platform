from django.contrib.auth.models import User
from django.db import models


class FriendRequest(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sent_friend_requests"
    )
    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="received_friend_requests"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["sender", "receiver"],
                name="unique_friend_request"
            )
        ]

    def __str__(self):
        return (
            f"{self.sender.username} → "
            f"{self.receiver.username}"
        )
    
class Follow(models.Model):
    follower = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following"
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="followers"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["follower", "following"],
                name="unique_follow"
            )
        ]

    def __str__(self):
        return (
            f"{self.follower.username} follows "
            f"{self.following.username}"
        )
    
class Notification(models.Model):
    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications"
    )
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sent_notifications"
    )
    notification_type = models.CharField(max_length=50)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.recipient.username}: {self.message}"