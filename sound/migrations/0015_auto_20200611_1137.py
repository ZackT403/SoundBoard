# Generated by Django 3.0.7 on 2020-06-11 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sound', '0014_auto_20200611_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soundpost',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
