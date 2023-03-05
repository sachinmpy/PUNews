from django.urls import path
from .views import *

urlpatterns = [
    path('global-feed/', global_feed, name='global_feed'),
    path('my-feed', my_feed, name='my_feed'),
    path('post-creation/', create_post, name='create_post'),
    path('post/delete/<slug:post_id>/', delete_post, name='delete_post'),
]