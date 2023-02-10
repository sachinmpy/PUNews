from django.shortcuts import render, HttpResponse, redirect
from .forms import NewsCreationForm
from django.contrib.auth.decorators import login_required
from .models import News
from user_models.models import User
from django.contrib import messages

import datetime

# Create your views here.
def indexpage(request):

    context = {
    }
   
    if request.user.is_authenticated:
        user = request.user
        context['user'] = user

        return render(request, 'news/indexpage.html', context)
   
    else:
        return render(request, 'news/indexpage.html', context)


def news(request):
    months = ['zero','January','February','March','April','May','June','July','August','September','October','November','December']
    today = datetime.date.today()
    
    all_news = News.objects.all().filter(
        posted_date__year=today.year,
        posted_date__month=today.month,
        is_approved = True,
    )[::-1]

    context = {
        'all_news': all_news,
        'current_month': months[today.month]
    }

    # if request.user.is_authenticated:
    #     context['user'] = request.user

    return render(request, 'news/news.html', context)


def view_news(request, news_id):
    news = News.objects.get(news_id=news_id)
    user = request.user
    context = {
        'news': news,
        'user': user,
    }
    return render(request, 'news/news_read.html', context)

@login_required(login_url='login_page')
def create_news(request):
    user = request.user
    form = NewsCreationForm(initial={'posted_by': user},instance=user)

    if request.method == 'POST':
        form = NewsCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("News Posted")
        else:
            return HttpResponse("Error")
    
    context = {
        'user': user,
        'form': form,
        'date': datetime.date.today(),
    }
    return render(request, 'news/news_creation.html', context)

def archives(request):
    months = ['zero','January','February','March','April','May','June','July','August','September','October','November','December']
    today = datetime.date.today()
    month = months[today.month]
    year = today.year

    news = News.objects.all()

    context = {
        'all_news': news,
    }
    return render(request, 'news/archives.html', context)

def approve_news(request, news_id):
    user = request.user

    if request.user.is_authenticated and user.designation == User.Designations.FACULTY and user.is_elevated:
        news = News.objects.get(news_id=news_id)
        news.is_approved = True
        news.approved_by = user
        news.save()

        messages.success(request, 'News Approved!!')
        return redirect('accept_news')  

    return HttpResponse('You are not Authenticated to Approve News!!')

def delete_news(request, news_id):
    user = request.user

    if request.user.is_authenticated and user.designation == User.Designations.FACULTY and user.is_elevated:
        news = News.objects.get(news_id=news_id)
        news.delete()

        messages.success(request, 'News Deleted!!')
        return redirect('accept_news')  

    news = News.objects.get(news_id=news_id)
    if request.user.is_authenticated and news.posted_by == user:
        news.delete()

        messages.success(request, 'News Deleted!!')
        return redirect('my_news')  

    return HttpResponse('You are not Authenticated to Delete News!!')