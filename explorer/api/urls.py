from django.urls import path
import api.views as api_views

app_name = 'api'
urlpatterns = [
    path('notes/', api_views.NoteListOrCreateView.as_view(), name='notebook'),
]
