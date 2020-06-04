from django.db import models


# Create your models here.
class SoundPost(models.Model):
    sound = models.FileField(upload_to='sounds')
    image = models.ImageField(upload_to='images', default='images/default.png')
    title = models.CharField(max_length=100, default='sound file')

    def __str__(self):
        return self.title
