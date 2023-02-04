from django.shortcuts import render, HttpResponse
from .forms import NewsCreationForm
from django.contrib.auth.decorators import login_required
from .models import News
from user_models.models import User

import datetime

# Create your views here.
def indexpage(request):

    context = {
    }
   
    if request.user.is_authenticated:
        user = request.user
        context['user'] = user

        return render(request, 'news/indexpage_loggedin.html', context)
   
    else:
        return render(request, 'news/indexpage_notloggedin.html', context)


def news(request):
    months = ['zero','January','February','March','April','May','June','July','August','September','October','November','December']
    today = datetime.date.today()
    
    all_news = News.objects.all().filter(
        posted_date__year=today.year,
        posted_date__month=today.month
    )
    context = {
        'all_news': all_news,
        'current_month': months[today.month]
    }

    # if request.user.is_authenticated:
    #     context['user'] = request.user

    return render(request, 'news/news.html', context)


def view_news(request, news_id):
    news = News.objects.get(news_id=news_id)

    context = {
        'news': news
    }
    return render(request, 'news/news_read.html', context)

@login_required(login_url='login_page')
def create_news(request):
    user = request.user
    form = NewsCreationForm(initial={
        'posted_by': user,
    })


    if request.method == 'POST':
        form = NewsCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("News Posted")
        else:
            return HttpResponse("Error")
    
    context = {
        'form': form,
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