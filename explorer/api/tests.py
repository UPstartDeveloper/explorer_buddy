from django.test import TestCase
from rest_framework.test import (
    APIRequestFactory, APITestCase
)
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from notes.models import Note
from api.serializers import NoteSerializer
import api.views as api_views


class NoteListOrCreateTests(APITestCase):
    def setUp(self):
        """Instance variables needed to test creating a Note
           as well as listing all Note objects in the API.
        """
        self.factory = APIRequestFactory()
        self.user = User.objects.create(username="Zain",
                                        email='zainr7989@gmail.com',
                                        password='Fake_passwords_for_days')
        self.view = api_views.NoteListOrCreate.as_view()

    def test_create_note(self):
        '''A user is able to create a single Note from this view.'''
        create_url = reverse('api:notebook')
        data = {'title': 'Test Note',
                'author': self.user.id,
                'content': 'This is a test note.'}
        post_request = self.factory.post(create_url, data)
        # test the Note is then created
        response = self.view(post_request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class NoteInspectionToolTests(APITestCase):
    def setUp(self):
        """Instance variables needed to test retrieving, editing,
           or deleting a Note instance.
        """
        self.factory = APIRequestFactory()
        self.user = User.objects.create(username="Zain",
                                        email='zainr7989@gmail.com',
                                        password='Fake_passwords_for_days')
        self.view = api_views.NoteListOrCreate.as_view()
        self.note = Note.objects.create(title='Test Note',
                                        author=self.user,
                                        content='This is a test note.')

    def test_retrieve_note(self):
        '''A user is able to view a Note instance by its unique id.'''
        read_url = reverse('api:note-tool', args=[self.note.id])
        get_request = self.factory.get(read_url)
        # test the JSON object is found
        response = self.view(get_request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
