from notes.models import Note
from django import forms


class NoteForm(forms.ModelForm):
    '''A form based on the Note model.'''
    class Meta:
        model = Note
        fields = ['title', 'content', 'media']

    # def __init__(self, *args, **kwargs):
        # super(NoteForm, self).__init__(*args, **kwargs)
