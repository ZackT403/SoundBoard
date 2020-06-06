from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import generic
from .forms import SignUpForm , DeletePost
from sound.models import SoundPost


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form = SignUpForm(request.POST)

            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                messages.success(request, f'Thanks for making an account {username}!')
                login(request, user)
                return redirect('main')

    else:
        form = SignUpForm()

    return render(request, 'users/signup.html', {'form': form})


class ProfileView(generic.View):

    @staticmethod
    def get(request):
        context = {
            'post': SoundPost.objects.filter(author=request.user),
        }
        template_name = 'users/profile.html'
        return render(request,'users/profile.html',context)


    @staticmethod
    def post(request):
        form = DeletePost(request.POST)

        if form.is_valid():
            data = form.cleaned_data['prim_key']
            SoundPost.objects.filter(pk=data).delete()
        return HttpResponseRedirect('/profile/')