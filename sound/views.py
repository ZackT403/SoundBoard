from django.views.generic import ListView, CreateView
from django.views import View
from .models import SoundPost, UserSoundBoard
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, HttpResponseRedirect
from .forms import ButtonForm, DeleteButton, SearchBar
from django.contrib.postgres.search import TrigramSimilarity
'''class MainView(ListView):
    template_name = 'sound/main.html'
    context_object_name = 'sound'
    model = UserSoundBoard

    def get_queryset(self):
        return SoundPost.objects.all().order_by('?')

    @staticmethod
    def post(request):
        form = ButtonForm(request.POST)
        if form.is_valid():
            pk_key = form.cleaned_data['val']
            post = SoundPost.objects.filter(pk=pk_key).first()
            model = UserSoundBoard(user=request.user, sounds=post)
            model.save()
        return HttpResponseRedirect('/')
'''


class MainView(View):

    @staticmethod
    def get(request):
        context = {
            'sound': SoundPost.objects.all().order_by('?'),
            'search': SearchBar(),
        }

        return render(request, 'sound/main.html',context)

    @staticmethod
    def post(request):
        form = ButtonForm(request.POST)
        search_qr = SearchBar(request.POST)

        if search_qr.is_valid():
            user_qr = search_qr.cleaned_data['search']
            results = SoundPost.objects.filter(title__contains = user_qr)
            context = {
                'sound': results,
                'search': search_qr,
            }
        else:
            context = {
                'sound': SoundPost.objects.all().order_by('?'),
                'search': search_qr,
            }

        if form.is_valid():
            pk_key = form.cleaned_data['val']
            post = SoundPost.objects.filter(pk=pk_key).first()
            model = UserSoundBoard(user=request.user, sounds=post)
            model.save()

        return render(request, 'sound/main.html', context)


class CreatePost(LoginRequiredMixin, CreateView):
    model = SoundPost
    success_url = '/'
    fields = ['title', 'sound', 'image']
    template_name = 'sound/postsound.html'

    def form_valid(self, form):
        audio = str(form.cleaned_data['sound'])
        audio_type = audio.split('.')[-1:][0]
        if 'mp3' not in audio_type:
            return HttpResponseRedirect('/new/')
        else:
            form.instance.author = self.request.user
            return super().form_valid(form)


class SoundBoard(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        user_sounds = UserSoundBoard.objects.filter(user=request.user)
        if not user_sounds.first():
            context = {
                'add_sounds': 'True',
            }
        else:
            context = {
                'user_sound': user_sounds,
            }

        return render(request, 'sound/sound_board.html', context)

    @staticmethod
    def post(request):
        form = DeleteButton(request.POST)
        if form.is_valid():
            prim_key = form.cleaned_data['prim_key']
            abso = UserSoundBoard.objects.filter(pk=prim_key).first()
            if request.user == abso.user:
                UserSoundBoard.objects.filter(pk=prim_key).first().delete()
        return HttpResponseRedirect('/soundboard/')


def handler404(request, *args, **kwargs):
    return render(request, 'error_pages/404.html', status=404)
