from django.urls import path
from notes.views import (
    NoteList, NoteDetail, NoteCreate, NoteUpdate, NoteDelete)
from django.conf import settings
from django.conf.urls.static import static

app_name = 'notes'
urlpatterns = ([
        # path('', NoteList.as_view(), name='notes-list-page'),
        path('', NoteCreate.as_view(), name="create_note_form"),
        path('<slug:slug>/edit/', NoteUpdate.as_view(), name="edit_note_form"),
        path('<slug:slug>/delete/', NoteDelete.as_view(), name='delete_note'),
        path('<slug:slug>/', NoteDetail.as_view(), name='notes-detail-page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
