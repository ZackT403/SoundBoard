from django.shortcuts import render
from django.views import View
from django.views import generic
from .models import SoundPost
from .forms import PostSound


class MainView(generic.ListView):
    template_name = 'sound/main.html'
    context_object_name = 'sound'

    def get_queryset(self):
        return SoundPost.objects.all().order_by('?')


class CreatePost(View):
    @staticmethod
    def get(request):
        context = {
            'form': PostSound(),
        }
        return render(request, 'sound/postsound.html', context)

    @staticmethod
    def post():
        pass
