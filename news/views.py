from django.shortcuts import render, HttpResponse
from .forms import NewsCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def indexpage(request):
    if request.user.is_authenticated:
        user = request.user
        context = {
            'user': user,
        }
        return render(request, 'news/indexpage_loggedin.html', context)
    else:
        context = {}
        return render(request, 'news/indexpage_notloggedin.html', context)


@login_required(login_url='login_page')
def create_news(request):
    user = request.user
    form = NewsCreationForm(initial={
        'posted_by': user,
    })
    context = {
        'form': form,
    }
    return render(request, 'news/news_creation.html', context)
