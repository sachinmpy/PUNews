from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
    path('', include('student.urls')),
    path('', include('faculty.urls')),
    path('', include('loginregister.urls')),
    path('', include('user_models.urls')),
    
]
