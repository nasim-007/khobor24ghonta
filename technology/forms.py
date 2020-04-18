from .models import TechnologyComment
from django import forms

class TechnologyCommentFrom(forms.ModelForm):
    class Meta:
        model = TechnologyComment
        fields = ('name', 'email', 'body')