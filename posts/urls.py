from django.urls import path
from .views import *

urlpatterns = [
    path('global-feed/', global_feed, name='global_feed'),
]