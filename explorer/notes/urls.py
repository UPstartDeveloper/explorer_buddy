from django.urls import path
from notes.views import (
    NoteList, NoteDetail, NoteCreate, NoteUpdate, NoteDelete)
from django.conf import settings
from django.conf.urls.static import static

app_name = 'notes'
urlpatterns = ([
        path('', NoteCreate.as_view(), name="create_note_form"),
        path('home/', NoteList.as_view(), name='index'),
        path('<slug:slug>/edit/', NoteUpdate.as_view(), name="edit_note_form"),
        path('<slug:slug>/delete/', NoteDelete.as_view(), name='delete_note'),
        path('<slug:slug>/', NoteDetail.as_view(), name='notes-detail-page'),
])

if settings.DEBUG is True:
    urlpatterns += [static(settings.MEDIA_URL,
                           document_root=settings.MEDIA_ROOT)]
    urlpatterns += [static(settings.STATIC_URL,
                           document_root=settings.STATIC_ROOT)]
