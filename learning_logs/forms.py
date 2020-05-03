from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """A class to define the topic form."""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': '', "public": "label for public"}

class EntryForm(forms.ModelForm):
    """A class to define the entry form."""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
