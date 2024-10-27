# models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.FileField(upload_to='profile_pictures/', null=True, blank=True)  # Changed to FileField

    def __str__(self):
        return f"{self.user.username}'s Profile"
