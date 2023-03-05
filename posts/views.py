from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostCreationForm
from .models import Post

# Create your views here.
def global_feed(request):
    context = {}

    global_post = Post.objects.all().filter(is_global=True) #CHANGED
    context['global_posts'] = global_post


    user = request.user
    if user.is_authenticated and not None:
        form = PostCreationForm(initial={'posted_by': request.user})
        context['form'] = form
        


    return render(request, 'post/global_feed.html', context)

@login_required(login_url='login_page')
def my_feed(request):
    user = request.user
    following = user.following.all()

    all_following_posts = []
    for follow in following:
        post = Post.objects.all().filter(posted_by=follow.following_user_id)
        all_following_posts.append(post)

    context = {
        'following': following
    }
    return render(request, 'post/my_feed.html', context)

@login_required(login_url='login_page')
def create_post(request):
    user = request.user
    
    if request.method == 'POST':
        form = PostCreationForm(request.POST, initial={'posted_by': user})
        print(form.data)
        if form.is_valid():
            form.save()

            return redirect("global_feed")
    
        else:
            return HttpResponse('Error')

@login_required(login_url='login_page')
def delete_post(request, post_id):
    user = request.user
    post = Post.objects.get(post_id=post_id)

    if post.posted_by == user and user.is_authenticated:
        post.delete()
        return redirect('my_posts')

    else:
        return HttpResponse("You cannot Delete this post")

