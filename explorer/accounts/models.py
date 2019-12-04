from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT,)
    mugshot = models.ImageField(upload_to='image/',
                                blank=True,
                                help_text="User profile image")

    def __str__(self):
        '''Return the related User's username.'''
        return self.user.username
