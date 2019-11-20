from django.urls import path
from notes.views import NoteList, NoteDetail
from django.conf import settings
from django.conf.urls.static import static

app_name = 'notes'
urlpatterns = [
        path('', NoteList.as_view(), name='notes-list-page'),
        path('<slug:slug>/', NoteDetail.as_view(), name='notes-detail-page')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
