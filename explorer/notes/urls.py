from django.urls import path
from notes.views import NoteList
from django.conf import settings
from django.conf.urls.static import static

app_name = 'notes'
urlpatterns = [
        path('', NoteList.as_view(), name='notes-list-page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
