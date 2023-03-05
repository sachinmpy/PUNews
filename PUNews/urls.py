from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),

    path('', include('news.urls')),
    path('', include('student.urls')),
    path('', include('faculty.urls')),
    path('', include('loginregister.urls')),
    path('', include('user_models.urls')),
    path('', include('profile_settings.urls')),
    path('', include('posts.urls')),
    
]
