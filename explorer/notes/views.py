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
        print(f'Media url: {explorer.settings.MEDIA_URL}')
        print(f'Media root: {explorer.settings.MEDIA_ROOT}')
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
        Return a response, using the `response_class` for NoteCreate, with a
        template rendered with the given context.
        Pass response_kwargs to the constructor of the response class.
        """
        response_kwargs.setdefault('content_type', self.content_type)
        notes = self.queryset
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

    # credit to Classy CBV for providing source code to override
    def render_to_response(self, context, **response_kwargs):
        """
        Return a response, using the `response_class` for NoteCreate, with a
        template rendered with the given context.
        Pass response_kwargs to the constructor of the response class.
        """
        response_kwargs.setdefault('content_type', self.content_type)
        notes = self.queryset
        notes_context = {'notes': notes}
        context.update(notes_context)
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            using=self.template_engine,
            **response_kwargs
        )

    '''
    def get(self, request, slug):
        """Renders a page to edit a note created previously.
           Parameters:
           slug(slug): specific slug of the Note instance.
           request(HttpRequest): the HTTP request sent to the server

           Returns:
           render: a page of the Note

        """
        note = self.queryset.get(slug__iexact=slug)
        notes = self.queryset
        context = {
            'note': note,
            'notes': notes
        }
        return super().get(request)
    '''
    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Note, slug=slug)
    '''
    '''


'''
    def form_valid(self, request, slug):
         note = Note.objects.get(slug=slug)
         note.title = request.POST.get('title', '')
         note.slug = request.POST.get('slug', '')
         note.content = request.POST.get('content', '')
         note.media = request.POST.get('media', '')
         note.modified = request.POST.get('modified', '')
         note.save()
         success_url = self.get_success_url()
         print(f'HEY! Object after submission: {obj}, success: {success_url}')
         return render(request, 'notes:notes-detail-page', {'slug': note.slug})
         return HttpResponseRedirect(reverse('notes:notes-detail-page',
                                     kwargs={'slug': note.slug}))

    def post(self, request, slug):
        """Override the CreateView post method, so that it invokes
           the subclass form_valid, which includes a parameter for request.
        """
        note = Note.objects.get(slug=slug)
        # print(n)

        if request.method == "POST":
            form = NoteForm(request.POST)
            if form.is_valid() is True:

                note.title = request.POST.get('title', '')
                note.slug = request.POST.get('slug', '')
                note.content = request.POST.get('content', '')
                note.media = request.POST.get('media', '')
                note.modified = request.POST.get('modified', '')


                note = form.save(commit=False)
                note.author = request.user
                note.modified = request.POST.get('modified', '')
                note.save()


                return HttpResponseRedirect(reverse('notes:notes-detail-page',
                                            kwargs={'slug': note.slug}))

        else:
            form = NoteForm(instance=note)

        return render(request, self.template_name, {'slug': note})

    def get_success_url(self):
        return reverse_lazy('notes:notes-detail-page', args=[self.object.slug])

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(f'HEY! Object before form submission: {self.object}')
        return super().get(self, request, *args, **kwargs)
    '''
'''
    def form_valid(self, form):
        clean_data = form.cleaned_data
        obj = self.object
        self.object = form.save()
        success_url = self.get_success_url()
        print(f'HEY! Object after submission: {obj}, success: {success_url}')
        return super().form_valid(form)
    '''


class NoteDelete(DeleteView):
    '''Render a form for user to delete a Note.'''
    model = Note
    template_name = 'notes/one_note.html'
    success_url = reverse_lazy('notes:create_note_form')
    queryset = Note.objects.all()

    def get(self, request, slug):
        """Renders a form to delete a Note.
           Parameters:
           slug(slug): specific slug of the Note instance.
           request(HttpRequest): the HTTP request sent to the server

           Returns:
           render: a page of the Note

        """
        notes = self.queryset
        note = self.queryset.get(slug__iexact=slug)
        context = {
            'notes': notes,
            'note': note
        }
        return render(request, self.template_name, context)
