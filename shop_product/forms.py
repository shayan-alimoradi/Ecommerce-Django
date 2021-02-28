from django import forms
from .models import *


class SearchForm(forms.Form):
    search = forms.CharField(max_length=177, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)