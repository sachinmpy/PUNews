from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from news.models import News

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


    context = {
        'user': user,
    }    

    return render(request, 'profile_settings/my_posts.html', context)

@login_required(login_url='login_page')
def followers(request):
    user = request.user
    

    context = {
        'user': user,
    }    

    return render(request, 'profile_settings/followers.html', context)

@login_required(login_url='login_page')
def following(request):
    user = request.user


    context = {
        'user': user,
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

