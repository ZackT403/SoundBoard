# Generated by Django 2.2.12 on 2020-06-05 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sound', '0011_soundpost_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSoundBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sounds', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sound.SoundPost')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]