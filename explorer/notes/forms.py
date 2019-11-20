from . import models
from django import forms


class NoteForm(forms.ModelForm):
    '''A form based on the Note model.'''
    class Meta:
        model = Note
        fields = ['title', 'content', 'media']
