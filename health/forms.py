from .models import HealthComment
from django import forms

class HealthCommentFrom(forms.ModelForm):
    class Meta:
        model = HealthComment
        fields = ('name', 'email', 'body')