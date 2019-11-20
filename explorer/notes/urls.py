from django.urls import path
from notes.views import NoteList

app_name = 'notes'
urlpatterns = [
        path('', NoteList.as_view(), name='notes-list-page'),
]
