from django.urls import path
from notes.views import NoteList, NoteDetail, NoteCreate
from django.conf import settings
from django.conf.urls.static import static

app_name = 'notes'
urlpatterns = [
        path('', NoteList.as_view(), name='notes-list-page'),
        path('create/', NoteCreate.as_view(), name="create_note_form"),
        path('<slug:slug>/', NoteDetail.as_view(), name='notes-detail-page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
