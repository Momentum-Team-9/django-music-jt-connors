from django import forms
from .models import Albums, Tracks

class AlbumForm(forms.ModelForm):

    class Meta:
        model = Albums
        fields = [
            'title', 
            'artist',
        ]

class TrackForm(forms.ModelForm):

    class Meta:
        model = Tracks
        fields = [
            'title'

        ]