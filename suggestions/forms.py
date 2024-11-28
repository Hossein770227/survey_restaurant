from django import forms

from .models import CommentsSuggestions

class CommentSuggestionsForm(forms.ModelForm):
    class Meta:
        model = CommentsSuggestions
        fields = ['text']