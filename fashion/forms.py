from .models import FashionComment
from django import forms

class FashionCommentFrom(forms.ModelForm):
    class Meta:
        model = FashionComment
        fields = ('name', 'email', 'body')