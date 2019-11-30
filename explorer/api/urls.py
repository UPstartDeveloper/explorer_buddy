from django.urls import path
import api.views as api_views

app_name = 'api'
urlpatterns = [
    path('notes/', api_views.NoteListOrCreate.as_view(), name='notebook'),
    path('notes/<int:pk>/', api_views.NoteInspectionTool.as_view(),
         name='note-tool'),
]
