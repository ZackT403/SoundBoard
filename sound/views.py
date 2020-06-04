from django.shortcuts import render
from django.views import View
from .models import SoundPost

# Create your views here.
class Main(View):
    @staticmethod
    def get(request):
        context = {
            'sound':SoundPost.objects.all(),
        }
        return render(request,'sound/main.html',context)
