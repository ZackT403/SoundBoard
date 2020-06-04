from django.shortcuts import render
from django.views import View

# Create your views here.
class Main(View):
    @staticmethod
    def get(request):
        return render(request,'sound/main.html')

    @staticmethod
    def post(request):
        pass