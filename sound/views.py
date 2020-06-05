from django.views.generic import ListView, CreateView
from .models import SoundPost
from django.contrib.auth.mixins import LoginRequiredMixin


class MainView(ListView):
    template_name = 'sound/main.html'
    context_object_name = 'sound'

    def get_queryset(self):
        return SoundPost.objects.all().order_by('?')


class CreatePost(LoginRequiredMixin, CreateView):
    model = SoundPost
    success_url = '/'
    fields = ['title', 'sound', 'image']
    template_name = 'sound/postsound.html'

    def form_valid(self, form):
        audio = str(form.cleaned_data['sound'])
        audio_type = audio.split('.')[-1:][0]
        if 'mp3' not in audio_type:
            print('not mp3')
        form.instance.author = self.request.user
        return super().form_valid(form)
