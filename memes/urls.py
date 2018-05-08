from django.conf.urls import url
from memes.views import MemeView
from . import views

app_name = 'meme'

urlpatterns = [
    url(r'^$', MemeView.as_view(), name='meme'),

]
