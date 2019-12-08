from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
import os
from explorer import settings


# Create your models here.
class Note(models.Model):
    """Represents a single note logged by a User."""
    title = models.CharField(max_length=settings.NOTE_TITLE_MAX_LENGTH,
                             unique=True,
                             help_text="Give your note a title to remember.")
    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               help_text="The explorer making this log.")
    slug = models.CharField(max_length=settings.NOTE_TITLE_MAX_LENGTH,
                            blank=True, editable=False,
                            help_text="Unique URL path to access this note." +
                                      "Computer Generated.")

    content = models.TextField(
        help_text="Log your observations, questions, and hypotheses here."
    )
    media = models.ImageField(upload_to='images/',
                              help_text="Optional image to add to note.",
                              blank=True,
                              null=True)
    created = models.DateTimeField(auto_now_add=True,
                                   help_text="The date and time this note " +
                                   "was created. Auto-generated.")
    modified = models.DateTimeField(auto_now_add=True,
                                    help_text="The date and time this note " +
                                              "was editied. Auto-calculated.")

    def __str__(self):
        '''Return the title of the note for ease of development.'''
        return self.title

    def get_absolute_url(self):
        '''Returns a fully qualified path for a page (i.e. /my-note).'''
        path_components = {'slug': self.slug}
        return reverse('notes:notes-detail-page', kwargs=path_components)

    def save(self, *args, **kwargs):
        '''Creates a URL safe slug automatically when a new note is saved.'''
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # call save on the superclass
        return super(Note, self).save(*args, **kwargs)
