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
    model = Note
    template_name = 'notes/one_note.html'

    def get(self, request, slug):
        """Renders a page to show a specific note in full detail.
           Parameters:
           slug(slug): specific slug of the Note instance.
           request(HttpRequest): the HTTP request sent to the server

           Returns:
           render: a page of the Note

        """
        note = self.get_queryset().get(slug__iexact=slug)
        context = {'note': note}
        return render(request, self.template_name, context)


class NoteCreate(CreateView):
    '''Render a form to create new note.'''
    pass


class NoteUpdate(UpdateView):
    '''Render a form to edit a note.'''
    pass


class NoteDelete(DeleteView):
    '''Render a form for user to delete a Note.'''
    pass
