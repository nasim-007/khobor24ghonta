from .models import PoliticsComment
from django import forms

class PoliticsCommentFrom(forms.ModelForm):
    class Meta:
        model = PoliticsComment
        fields = ('name', 'email', 'body')