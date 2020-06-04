from django.shortcuts import render
from django.views import View
from .models import SoundPost
from .forms import PostSound
# Create your views here.
class Main(View):
    @staticmethod
    def get(request):
        context = {
            'sound':SoundPost.objects.all(),
        }
        return render(request,'sound/main.html',context)

class CreatePost(View):

    @staticmethod
    def get(request):
        context = {
            'form':PostSound(),
        }
        return render(request,'sound/postsound.html',context)
    @staticmethod
    def post():
        pass