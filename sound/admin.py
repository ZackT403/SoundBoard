from django.contrib import admin
from .models import SoundPost,UserSoundBoard

# Register your models here.
admin.site.register(SoundPost)
admin.site.register(UserSoundBoard)