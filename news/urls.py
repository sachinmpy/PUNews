from django.urls import path
from .views import indexpage, create_news, news, view_news, archives, approve_news, delete_news

urlpatterns = [
    path('', indexpage, name='indexpage'),
    path('news', news, name='news'),
    path('create-news', create_news, name='create_news'),
    path('news/<slug:news_id>', view_news, name='view_news'),
    path('archives', archives, name='archives'),
    path('news/approve/<slug:news_id>', approve_news, name='approve_news'),
    path('news/delete/<slug:news_id>', delete_news, name='delete_news'),

]