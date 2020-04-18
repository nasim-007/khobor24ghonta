from .models import BangladeshComment
from django import forms

class BangladeshCommentFrom(forms.ModelForm):
    class Meta:
        model = BangladeshComment
        fields = ('name', 'email', 'body')