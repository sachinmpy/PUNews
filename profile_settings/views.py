from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from news.models import News
from posts.models import Post
from user_models.models import Followings, User

from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@login_required(login_url='login_page')
def user_settings(request):
    user = request.user


    context = {
        'user': user,
    }
    return render(request, "profile_settings/user_settings.html", context)


@login_required(login_url='login_page')
def my_news(request):
    user = request.user
    approved_news = News.objects.all().filter(
        posted_by = user,
        is_approved = True
    )

    unapproved_news = News.objects.all().filter(
        posted_by = user,
        is_approved = False
    )

    context = {
        'user': user,
        'approved_news': approved_news,
        'unapproved_news': unapproved_news,
    }    

    return render(request, 'profile_settings/my_news.html', context)

@login_required(login_url='login_page')
def my_posts(request):
    user = request.user
    posts = Post.objects.all().filter(posted_by=user)

    context = {
        'user': user,
        'posts': posts,
    }    

    return render(request, 'profile_settings/my_posts.html', context)

@login_required(login_url='login_page')
def followers(request):
    user = request.user
    all_followers = user.follower.all()
    print(all_followers)
    context = {
        'user': user,
        'all_followers': all_followers,
    }    

    return render(request, 'profile_settings/followers.html', context)

@login_required(login_url='login_page')
def following(request):
    user = request.user
    all_following = user.following.all()

    context = {
        'user': user,
        'all_following': all_following,
    }    

    return render(request, 'profile_settings/following.html', context)

@login_required(login_url='login_page')
def accept_news(request):
    user = request.user
    pending_news = News.objects.all().filter(is_approved=False)

    context = {
        'user': user,
        'pending_news': pending_news,
    }    

    return render(request, 'profile_settings/accept_news.html', context)

login_required(login_url='login_page')
def follow(request, following_user_id):
    print('follow function and: ', following_user_id)
    follow_user = User.objects.get(username=following_user_id)
    Followings.objects.create(
        user_id=request.user,
        following_user_id=follow_user
    )
    return redirect('user_profile', usrname=follow_user)

login_required(login_url='login_page')
def unfollow(request, following_user_id):
    follow_user = User.objects.get(username=following_user_id)
    try:
        f = Followings.objects.get(user_id=request.user, following_user_id=follow_user)
        f.delete()
        return redirect('user_profile', usrname=follow_user)
   
    except ObjectDoesNotExist:
        return HttpResponse("Error Has Occured")
    