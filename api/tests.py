from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Note


class NoteTests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Log in the test client
        self.client.login(username='testuser', password='testpassword')

    def test_create_note(self):
        """
        Ensure we can create a new note object.
        """
        url = reverse('notes-list')
        data = {'id': 1, 'title': 'Note 1', 'content': 'This is note #1.', 'created_at': '2021-01-01T00:00:00Z'}
        self.client.login(username='admin', password='password123')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 1)
        self.assertEqual(Note.objects.get().title, 'Note 1')
