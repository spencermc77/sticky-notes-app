from django.test import TestCase
from django.urls import reverse
from .models import Note

class NoteTests(TestCase):
    def test_note_model(self):
        note = Note.objects.create(title="Test Title", content="Test Content")
        self.assertEqual(note.title, "Test Title")
        self.assertEqual(note.content, "Test Content")

    def test_note_list_view(self):
        Note.objects.create(title="Note 1", content="Content 1")
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Note 1")

    def test_create_note_view(self):
        response = self.client.post(reverse('create_note'), {
            'title': 'New Note',
            'content': 'New Content'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 1)
        self.assertEqual(Note.objects.first().title, 'New Note')

    def test_delete_note_view(self):
        note = Note.objects.create(title="Delete Me", content="Remove this")
        response = self.client.get(reverse('delete_note', args=[note.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 0)