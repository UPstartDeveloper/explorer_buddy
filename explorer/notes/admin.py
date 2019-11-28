from django.contrib import admin
from .models import Note

# Register your models here.
admin.site.register(Note)
admin.site.site_header = 'Explorer Buddy Support'
