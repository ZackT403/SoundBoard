from django import forms

class PostSound(forms.Form):
    title = forms.CharField(max_length=20)
    sound = forms.FileField()
    image = forms.ImageField()