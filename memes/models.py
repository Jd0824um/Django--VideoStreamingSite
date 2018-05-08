from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Post(models.Model):
    text = models.CharField(max_length=500)
    image = models.ImageField(upload_to= 'media/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(auto_now=True, blank=True)
