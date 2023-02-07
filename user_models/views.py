from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from user_models.models import User
from news.models import News

import random
# Create your views here.

banner_urls = [
    'https://static.vecteezy.com/system/resources/previews/005/048/576/non_2x/abstract-background-banner-with-color-creative-digital-light-modern-free-vector.jpg',
    'https://png.pngtree.com/thumb_back/fh260/back_pic/00/02/44/5056179b42b174f.jpg',
    
]
    

# @login_required(login_url='login_page')
def user_profile(request, usrname): #HINT: LOOK FOR MAL OR ANILIST
    user = User.objects.get(username=usrname)
    designation = user.designation
    all_news = News.objects.all().filter(posted_by=user, is_approved=True)
    
    context = {
        'user': user,
        'designation': designation,
        'banner': random.choice(banner_urls),
        'all_news': all_news,
    }
    return render(request, 'user_models/user_profile.html', context)

    #NEEDS TO IMPLEMENT PROFILE SETTING




# Helpers Functions:
# def get_user_details(user):
#     details = {}
#     user = User.objects.get(username=user)
    
#     if user.designation == 'STUDENT':

#         details = {
#             'username': user.username,
#             'first_name': user.first_name,
#             'last_name': user.last_name,
#             'designation': user.designation,
#             'department': user.department,
#             'email': user.email,
#             'date_joined': user.date_joined,
#             'is_elevated': user.is_elevated,
#             'current_year': user.studentprofile.current_year,
#         }
    
#     elif user.designation == 'FACULTY':

#         details = {
#             'username': user.username,
#             'first_name': user.first_name,
#             'last_name': user.last_name,
#             'designation': user.designation,
#             'department': user.department,
#             'email': user.email,
#             'date_joined': user.date_joined,
#             'is_elevated': user.is_elevated,
#         }

#     return details