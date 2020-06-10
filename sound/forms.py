from django import forms
from .models import SoundPost


class ButtonForm(forms.Form):
    val = forms.CharField()


class DeleteButton(forms.Form):
    prim_key = forms.CharField()


class SearchBar(forms.Form):
    search = forms.CharField(max_length=20)