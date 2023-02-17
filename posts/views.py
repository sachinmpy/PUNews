from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PostCreationForm
from .models import Post

# Create your views here.
def global_feed(request):
    context = {}

    global_post = Post.objects.all().filter(is_global=True)
    context['global_posts'] = global_post


    user = request.user
    if user.is_authenticated and not None:
        form = PostCreationForm()
        context['form'] = form
        


    return render(request, 'post/global_feed.html', context)


@login_required(login_url='login_page')
def create_post(request):
    pass