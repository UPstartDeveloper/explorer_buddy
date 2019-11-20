from django.shortcuts import render
from django.views.generic.list import ListView
from notes.models import Note


class NoteList(ListView):
    '''Renders a list of all Notes.'''
    model = Note
    template_name = 'notes/notebook.html'
