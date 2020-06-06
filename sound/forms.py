from django import forms
from .models import SoundPost


class ButtonForm(forms.Form):
    val = forms.CharField()