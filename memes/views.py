from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist
from memes.forms import MemeForm
from memes.models import Post
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import Http404

class MemeView(TemplateView):
    template_name = 'meme/meme.html'

    def get(self, request):
        form = MemeForm()
        posts = Post.objects.filter(user=request.user).order_by('-created')

        return render(request, self.template_name, {'form' : form, 'posts' : posts})

    def post(self, request):
        if request.method == 'POST':
            form = MemeForm(request.POST, request.FILES)

            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                form = MemeForm()
                return redirect('home:home')
            else:
                raise Http404

        return render(request, self.template_name, {'form' : form})
