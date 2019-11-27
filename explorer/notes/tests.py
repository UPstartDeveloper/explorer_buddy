from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from notes.models import Note
from django.urls import reverse
from notes.views import NoteCreate


class NoteCreateTests(TestCase):
    '''A user can insert a new note into the database.'''
    def setUp(self):
        '''Instaniate RequestFactory and User to make POST requests.'''
        self.factory = RequestFactory()
        self.user = User.objects.create(username='Zain',
                                        email='zain_14@icloud.com',
                                        password='bismillah')
