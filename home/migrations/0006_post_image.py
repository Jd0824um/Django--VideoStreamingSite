# Generated by Django 2.0.5 on 2018-05-06 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_friend_current_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=False, upload_to=''),
        ),
    ]
