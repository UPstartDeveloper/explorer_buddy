from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from notes.models import Note
from django.urls import reverse, reverse_lazy
from notes.views import NoteCreate, NoteDetail, NoteUpdate, NoteDelete
from django.shortcuts import render


class NoteCreateTests(TestCase):
    '''A user can insert a new note into the database.'''
    def setUp(self):
        '''Instaniate RequestFactory and User to make requests.'''
        self.factory = RequestFactory()
        self.user = User.objects.create(username='Zain',
                                        email='zain_14@icloud.com',
                                        password='bismillah')

    def test_post_new_note(self):
        '''A new note exists after the user submits the form.'''
        # simulate data the user types into the form
        form_data = {
            'title': 'Frogs',
            'content': 'What makes a frog tongue so strong?',
        }

        # simulate the user clicking 'Submit' on the form
        post_request = self.factory.post('notes:create_note_form', form_data)
        post_request.user = self.user
        response = NoteCreate.as_view()(post_request)
        # test the view redirects to the details page
        self.assertEqual(response.status_code, 302)
        # test that the database contains the new Page
        note = Note.objects.last()
        self.assertEqual(note.title, 'Frogs')
        self.assertEqual(note.slug, 'frogs')


class NoteDetailViewTests(TestCase):
    '''A user can view the details of a specific note.'''
    def setUp(self):
        '''Instaniate User for required author field in Note objects.'''
        self.user = User.objects.create(username='Zain',
                                        email='zain_14@icloud.com',
                                        password='bismillah')
        self.factory = RequestFactory()

    def test_get_details_for_one_note(self):
        """The details included for a specific note are accurate
           with what's in the database, and for that note only.

        """
        # simulate creation of a note (like before)
        note = Note.objects.create(title='Frogs',
                                   content='Why do frogs eat flies?',
                                   author=self.user,
                                   media=None)
        self.assertEqual(note.slug, 'frogs')

        # GET the details of the object
        get_request = self.factory.get('/notes/frogs')
        get_request.user = self.user
        response = NoteDetail.as_view()(get_request, note.slug)
        # test the data that renders
        self.assertEqual(len(Note.objects.filter(title="Frogs")), 1)

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Frogs')

        inserted_note = Note.objects.get(title='Frogs')
        self.assertEqual(note.created, inserted_note.created)


class NoteUpdateTests(TestCase):
    '''A user can change the fields for a specific Note.'''
    def setUp(self):
        '''Instaniate User for required author field in Note objects.'''
        self.user = User.objects.create(username='Zain',
                                        email='zain_14@icloud.com',
                                        password='bismillah')
        self.factory = RequestFactory()
        self.note = Note.objects.create(title='Frogs',
                                        content='Why do frogs eat flies?',
                                        author=self.user,
                                        media=None)

    def test_get_update_form(self):
        '''A user sees the edit form prepopulated with the current data.'''
        # add a Note, make sure it's slug is generated
        self.assertEqual(self.note.slug, 'frogs')
        # the user can see the page using the slug of the Note in the URL
        get_request = self.factory.get('/notes/frogs/edit/')
        get_request.user = self.user
        response = NoteUpdate.as_view()(get_request, slug=self.note.slug)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Frogs')

    def test_edit_note_redirect(self):
        '''After a valid form submission, the user is redirected.'''
        previous_content = self.note.content
        # user enters data they want to replace current Note data
        new_content = "What makes a frog's tongue so sticky?"
        form_data = {
            'content': new_content
        }
        # user submits the form
        post_request = self.factory.post('/notes/frogs/edit/', form_data)
        post_request.user = self.user
        response = NoteUpdate.as_view()(post_request, slug=self.note.slug)
        # the data in the field of the corresponding Note changes
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.note.content, new_content)


class NoteDeletionTests(TestCase):
    '''A user can delete a Note.'''
    def setUp(self):
        '''Instaniate User for required author field in Note objects.'''
        self.user = User.objects.create(username='Zain',
                                        email='zain_14@icloud.com',
                                        password='bismillah')
        self.factory = RequestFactory()
        self.note = Note.objects.create(title='Frogs',
                                        content='Why do frogs eat flies?',
                                        author=self.user,
                                        media=None)
        self.note.save()

    def test_get_delete_page(self):
        '''A user is able to see a page asking them to confirm deletion.'''
        get_request = self.factory.get('notes:delete_note')
        get_request.user = self.user
        response = NoteDelete.as_view()(get_request, slug=self.note.slug)
        self.assertEqual(response.status_code, 200)


class NoteListTests(TestCase):
    pass
