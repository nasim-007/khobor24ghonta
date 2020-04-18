from .models import FunnyComment
from django import forms

class FunnyCommentFrom(forms.ModelForm):
    class Meta:
        model = FunnyComment
        fields = ('name', 'email', 'body')