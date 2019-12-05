from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (ModelFormMixin, CreateView, UpdateView,
                                       DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from notes.models import Note
from django.contrib.auth.models import User
from notes.forms import NoteForm
import explorer


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
        # print(f'Static dir: {explorer.settings.STATICFILES_DIRS[0]}')
        # print(f'Static root: {explorer.settings.STATIC_ROOT}')
        # print(f'Media url: {explorer.settings.MEDIA_URL}')
        # print(f'Media root: {explorer.settings.MEDIA_ROOT}')
        note = self.get_queryset().get(slug__iexact=slug)
        notes = self.get_queryset().all()
        context = {
            'note': note,
            'notes': notes
        }
        return render(request, self.template_name, context)


class NoteCreate(CreateView):
    '''Render a form to create new note.'''
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_create_form.html'
    queryset = Note.objects.all()

    # credit to Classy CBV for providing source code to override
    def render_to_response(self, context, **response_kwargs):
        """
        Allows for other notes to appear on sidebar.
        Return a response, using the `response_class` for NoteCreate, with a
        template rendered with the given context.
        Pass response_kwargs to the constructor of the response class.
        """
        response_kwargs.setdefault('content_type', self.content_type)
        notes = Note.objects.all()
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
        '''Initializes author of new Note by tracking the logged in user.'''
        # assert self.request.user.is_authenticated is True
        form.instance.author = self.request.user
        return super().form_valid(form)


'''
def update(request, slug):
    instance = get_object_or_404(Note, slug=slug)
    form = NoteForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        note = Note.objects.get(slug=instance.slug)
        return redirect(reverse('notes/note_edit_form.html', note.slug))
    return render(request, 'notes/note_edit_form.html', {'form': form})
'''


class NoteUpdate(UpdateView):
    '''Render a form to edit a note.'''
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_edit_form.html'
    queryset = Note.objects.all()

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(self.get_queryset().all())
        return super().get(request, *args, **kwargs)

    # credit to Classy CBV for providing source code to override
    def render_to_response(self, context, **response_kwargs):
        """
        Allows for other notes to appear on sidebar.
        Return a response, using the `response_class` for NoteUpdate, with a
        template rendered with the given context.
        Pass response_kwargs to the constructor of the response class.
        """
        response_kwargs.setdefault('content_type', self.content_type)
        notes = Note.objects.all()
        notes_context = {'notes': notes}
        context.update(notes_context)
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            using=self.template_engine,
            **response_kwargs
        )


class NoteDelete(DeleteView):
    '''Render a form for user to delete a Note.'''
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('notes:create_note_form')
    queryset = Note.objects.all()

    def get(self, request, slug):
        """Renders a form to delete a Note.
           Parameters:
           slug(slug): specific slug of the Note instance.
           request(HttpRequest): the HTTP request sent to the server

           Returns:
           render: a page to confirm deletion

        """
        notes = self.queryset
        note = self.queryset.get(slug__iexact=slug)
        context = {
            'notes': notes,
            'note': note
        }
        return render(request, self.template_name, context)
