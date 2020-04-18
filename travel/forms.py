from travel.models import TravelComment
from django import forms

class TravelCommentFrom(forms.ModelForm):
    class Meta:
        model = TravelComment
        fields = ('name', 'email', 'body')