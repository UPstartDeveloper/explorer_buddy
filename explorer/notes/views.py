from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (ModelFormMixin, CreateView, UpdateView,
                                       DeleteView)
from django.http import HttpResponseRedirect
from notes.models import Note
from django.contrib.auth.models import User
from notes.forms import NoteForm


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
    form_class = NoteForm
    template_name = 'notes/note_create_form.html'

    def form_valid(self, form, request):
        """Creates the new Note, and makes the user who submitted
           the form the author.
        """
        self.object = form.save(commit=False)
        user = User.objects.get(username=request.user)
        self.object.author = user
        self.object = form.save()
        return super(ModelFormMixin, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        """Override the CreateView post method, so that it invokes
           the subclass form_valid, which includes a parameter for request.
        """
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, request)
        else:
            return self.form_invalid(form)


class NoteUpdate(UpdateView):
    '''Render a form to edit a note.'''
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_edit_form.html'

    # def form_valid(self, request, slug):
    #     note = Note.objects.get(slug=slug)
    #     note.title = request.POST.get('title', '')
    #     note.slug = request.POST.get('slug', '')
    #     note.content = request.POST.get('content', '')
    #     note.media = request.POST.get('media', '')
    #     note.modified = request.POST.get('modified', '')
    #     note.save()
    #     success_url = self.get_success_url()
    #     print(f'HEY! Object after submission: {obj}, success: {success_url}')
    #     return render(request, 'notes:notes-detail-page', {'slug': note.slug})
    # return HttpResponseRedirect(reverse('notes:notes-detail-page', kwargs={'slug': note.slug}))

    def post(self, request, slug):
        """Override the CreateView post method, so that it invokes
           the subclass form_valid, which includes a parameter for request.
        """
        note = Note.objects.get(slug=slug)
        # print(n)

        if request.method == "POST":
            form = NoteForm(request.POST)
            if form.is_valid() is True:

                # note.title = request.POST.get('title', '')
                # note.slug = request.POST.get('slug', '')
                # note.content = request.POST.get('content', '')
                # note.media = request.POST.get('media', '')
                # note.modified = request.POST.get('modified', '')


                note = form.save(commit=False)
                note.author = request.user
                note.modified = request.POST.get('modified', '')
                note.save()


                return HttpResponseRedirect(reverse('notes:notes-detail-page', kwargs={'slug': note.slug}))

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
    pass
