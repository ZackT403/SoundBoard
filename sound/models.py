from django.db import models

# Create your models here.
class SoundPost(models.Model):
    sound = models.FileField(upload_to='sounds')