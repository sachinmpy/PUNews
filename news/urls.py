from django.urls import path
from .views import indexpage, create_news, news, view_news, archives

urlpatterns = [
    path('', indexpage, name='indexpage'),
    path('news', news, name='news'),
    path('create-news', create_news, name='create_news'),
    path('news/<slug:news_id>', view_news, name='view_news'),
    path('archives', archives, name='archives')
]