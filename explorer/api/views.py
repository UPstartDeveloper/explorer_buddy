from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from notes.models import Note
from api.serializers import NoteSerializer


class NoteListOrCreateView(ListCreateAPIView):
    """Presents a list of all Note instances.
       Allows for the creation of single Note.
       Method handlers for GET and POST.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
