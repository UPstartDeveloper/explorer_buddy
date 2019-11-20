from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone


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
    media = models.ImageField(upload_to='media', help_text="Optional image to add to note.")
    created = models.DateTimeField(auto_now_add=True,
                                   help_text="The date and time this note " +
                                             "was created. Auto-generated.")
    modified = models.DateTimeField(auto_now_add=True,
                                    help_text="The date and time this note " +
                                              "was editied. Auto-calculated.")
