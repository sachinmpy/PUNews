from django.urls import path
from .views import user_profile, user_settings

urlpatterns = [
    path('profile/<str:usrname>', user_profile, name='user_profile'),
    path('profile/settings/<str:username>', user_settings, name='user_settings'),
]