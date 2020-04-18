from .models import EducationComment
from django import forms

class EducationCommentFrom(forms.ModelForm):
    class Meta:
        model = EducationComment
        fields = ('name', 'email', 'body')