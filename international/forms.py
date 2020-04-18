from .models import InternationalComment
from django import forms

class InternationalCommentFrom(forms.ModelForm):
    class Meta:
        model = InternationalComment
        fields = ('name', 'email', 'body')