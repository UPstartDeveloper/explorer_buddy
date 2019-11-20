from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from notes.models import Note


class NoteList(ListView):
    '''Renders a list of all Notes.'''
    model = Note
    template_name = 'notes/notebook.html'

    def get(self, request):
        ''' Get a list of all notes currently in the database.'''
        notes = self.get_queryset().all()
        return render(request, self.template_name, {
            'notes': notes
        })


class NoteDetail(DetailView):
    '''Display the information currently on one Note.'''
    pass


class NoteCreate(CreateView):
    '''Render a form to create new note.'''
    pass


class NoteUpdate(UpdateView):
    '''Render a form to edit a note.'''
    pass


class NoteDelete(DeleteView):
    '''Render a form for user to delete a Note.'''
    pass
