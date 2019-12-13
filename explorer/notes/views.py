from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from notes.models import Note
from django.contrib.auth.models import User
from notes.forms import NoteForm
import explorer


class NoteList(ListView):
    '''Renders a list of all Notes.'''
    model = Note
    template_name = 'notes/notebook.html'
    login_url = 'accounts:login'

    def get(self, request):
        ''' Get a list of all notes currently in the database.'''
        notes = self.get_queryset().filter(author=request.user)
        return render(request, self.template_name, {
            'notes': notes
        })


class NoteDetail(DetailView):
    '''Display the information currently on one Note.'''
    model = Note
    template_name = 'notes/one_note.html'
    login_url = 'accounts:login'

    def get(self, request, slug):
        """Renders a page to show a specific note in full detail.
           Parameters:
           slug(slug): specific slug of the Note instance.
           request(HttpRequest): the HTTP request sent to the server

           Returns:
           render: a page of the Note

        """
        note = self.get_queryset().get(slug__iexact=slug)
        notes = self.get_queryset().filter(author=request.user)
        context = {
            'note': note,
            'notes': notes
        }
        return render(request, self.template_name, context)


class NoteCreate(CreateView):
    '''Submit a form to create new note.'''
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_create_form.html'
    queryset = Note.objects.all()
    login_url = 'accounts:login'

    # credit to Classy CBV for providing source code to override
    def render_to_response(self, context, **response_kwargs):
        """
        Allows for other notes to appear on sidebar.
        Return a response, using the `response_class` for NoteCreate, with a
        template rendered with the given context.
        Pass response_kwargs to the constructor of the response class.
        """
        response_kwargs.setdefault('content_type', self.content_type)
        notes = Note.objects.filter(author=self.request.user)
        notes_context = {'notes': notes}
        context.update(notes_context)
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            using=self.template_engine,
            **response_kwargs
        )

    def form_valid(self, form):
        '''Initializes author and image (if there is one) of new Note.'''
        form.instance.author = self.request.user
        form.instance.media = self.request.FILES.get('media')
        return super().form_valid(form)


class NoteUpdate(UpdateView):
    '''Submit a form to edit a note.'''
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_edit_form.html'
    queryset = Note.objects.all()
    login_url = 'accounts:login'

    # credit to Classy CBV for providing source code to override
    def render_to_response(self, context, **response_kwargs):
        """
        Allows for other notes to appear on sidebar.
        Return a response, using the `response_class` for NoteUpdate, with a
        template rendered with the given context.
        Pass response_kwargs to the constructor of the response class.
        """
        response_kwargs.setdefault('content_type', self.content_type)
        notes = self.queryset.filter(author=self.request.user)
        notes_context = {'notes': notes}
        context.update(notes_context)
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            using=self.template_engine,
            **response_kwargs
        )

    def test_func(self):
        '''Checks that the user updating the note is its author.'''
        note = self.get_object()
        return (self.request.user == note.author)

    def form_valid(self, form):
        '''Changes the image (if there is a new uploadd) of the Note.'''
        form.instance.media = self.request.FILES.get('media')
        return super().form_valid(form)


class NoteDelete(DeleteView):
    '''User is able to delete a Note.'''
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('notes:create_note_form')
    queryset = Note.objects.all()
    login_url = 'accounts:login'

    def get(self, request, slug):
        """Renders a form to delete a Note.
           Parameters:
           slug(slug): specific slug of the Note instance.
           request(HttpRequest): the HTTP request sent to the server

           Returns:
           render: a page to confirm deletion

        """
        notes = self.queryset.filter(author=request.user)
        note = self.queryset.get(slug__iexact=slug)
        context = {
            'notes': notes,
            'note': note
        }
        return render(request, self.template_name, context)

    def test_func(self):
        '''Checks that the user deleting the note is its author.'''
        note = self.get_object()
        return (self.request.user == note.author)
