from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(
        upload_to="profile_pics/",
        blank=True,
        null=True
    )
    cover_photo = models.ImageField(
        upload_to="cover_photos/",
        blank=True,
        null=True
    )
    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} Profile"