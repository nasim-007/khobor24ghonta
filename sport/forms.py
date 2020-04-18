from .models import SportComment
from django import forms

class SportCommentFrom(forms.ModelForm):
    class Meta:
        model = SportComment
        fields = ('name', 'email', 'body')