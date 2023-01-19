from django.urls import path
from .views import indexpage, create_news

urlpatterns = [
    path('', indexpage, name='indexpage'),
    path('create-news', create_news, name='create_news'),
]