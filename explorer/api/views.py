from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from notes.models import Note
from api.serializers import NoteSerializer


class NoteListOrCreate(ListCreateAPIView):
    """Presents a list of all Note instances.
       Allows for the creation of single Note.
       Method handlers for GET and POST.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteInspectionTool(RetrieveUpdateDestroyAPIView):
    """User is able to read, update, or delete a Note instance.
       Lookup uses the id field of the specific Note object.
        Work with GET, PUT, PATCH, or DELETE methods.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
