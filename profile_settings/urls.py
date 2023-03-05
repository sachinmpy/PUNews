from django.urls import path
from .views import *

urlpatterns = [
    path('profile/settings/edit-profile', user_settings, name='user_settings'),
    path('profile/settings/my-news', my_news, name='my_news'),
    path('profile/settings/my-posts', my_posts, name='my_posts'),
    path('profile/settings/followers', followers, name='followers'),
    path('profile/settings/following', following, name='following'),
    path('profile/settings/accept-news', accept_news, name='accept_news'),

    # Should be moved to its own app in future
    path('follow/<str:following_user_id>', follow, name='follow'),
    path('unfollow/<str:following_user_id>', unfollow, name='unfollow'),
]