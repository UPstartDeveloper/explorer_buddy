from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

"""
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT,)
    mugshot = models.ImageField(upload_to='image/',
                                blank=True,
                                help_text="User profile image")

    def create_profile(sender, **kwargs):
        '''Instanitate a Profile for each new user who signs up.'''
        if kwargs['created'] is not None:
            profile = Profile.objects.create(user=kwargs['accounts_profile.user_id'])

    post_save.connect(create_profile, sender=User)

    def __str__(self):
        '''Return the related User's username.'''
        return self.user.username

"""
