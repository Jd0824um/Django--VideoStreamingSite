# Generated by Django 2.0.5 on 2018-05-07 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memes', '0004_auto_20180507_0302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated',
        ),
    ]
