from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from notes.models import Note
from django.urls import reverse
from notes.views import NoteCreate, NoteDetail


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
        self.note.save()


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
