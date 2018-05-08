from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist
from home.models import Friend
from memes.models import Post
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        posts = Post.objects.all().order_by('-created')
        users = User.objects.exclude(id=request.user.id)
        try:
            friend = Friend.objects.get(current_user=request.user)
            friends = friend.users.all()
        except Friend.DoesNotExist:
            friends = None
        return render(request, self.template_name, {'posts' : posts, 'users' : users, 'friends': friends})

def update_friend(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('home:home')
