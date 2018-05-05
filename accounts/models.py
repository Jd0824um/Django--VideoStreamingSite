from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from localflavor.us.models import USStateField
from django.utils import timezone

# Creates a user profile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=150, default='')
    city = models.CharField(max_length=20, default='')
    state = USStateField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    phone = models.IntegerField(default=0)
    profile_picture = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.user.username

# Associates the user that's being created with the user profile
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
