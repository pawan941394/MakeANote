from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Note, UserProfile

class CreateUserForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'phone', 'linkedin', 'instagram', 'image']



class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['note_title','note_content', 'image', 'video']
        widgets = {
            'note_title': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }
        def __init__(self, *args, **kwargs):
            super(NoteForm, self).__init__(*args, **kwargs)
            self.fields['video'].widget.attrs.update({'class': 'myfieldclassvideo'})
            self.fields['image'].widget.attrs.update({'class': 'myfieldclassvideo'})
      
