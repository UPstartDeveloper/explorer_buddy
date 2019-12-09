from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from explorer import settings
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mugshot = models.ImageField(upload_to='images/',
                                default='images/user-icon.png',
                                help_text="User profile image")

    def __str__(self):
        '''Return the related User's username.'''
        return f"{self.user.username}'s Profile"

    def get_absolute_url(self):
        '''Returns a fully qualified path for a profile (i.e. /my-note).'''
        path_components = {'pk': self.user.id}
        return reverse('accounts:user_info', kwargs=path_components)
