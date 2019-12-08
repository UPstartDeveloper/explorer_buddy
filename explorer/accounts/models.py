from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from explorer import settings


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mugshot = models.ImageField(upload_to='images/',
                                default='images/user-icon.png',
                                help_text="User profile image")

    def __str__(self):
        '''Return the related User's username.'''
        return f"{self.user.username}'s Profile"
