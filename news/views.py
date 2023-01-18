from django.shortcuts import render, HttpResponse

# Create your views here.
def home_page(request):
    context = {}
    return render(request, 'news/landing_page.html', context)