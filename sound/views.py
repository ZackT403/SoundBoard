from django.shortcuts import render
from django.views import View
from django.views import generic
from .models import SoundPost
from django.shortcuts import HttpResponseRedirect
from django.views.generic import CreateView

class MainView(generic.ListView):
    template_name = 'sound/main.html'
    context_object_name = 'sound'

    def get_queryset(self):
        return SoundPost.objects.all().order_by('?')


class CreatePost(CreateView):
    model = SoundPost
    success_url = '/'
    fields = ['title','sound','image']
    template_name = 'sound/postsound.html'
    def  form_valid(self, form):
        return super().form_valid(form)