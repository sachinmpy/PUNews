from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from user_models.models import User, Followings
from django.core.exceptions import ObjectDoesNotExist
from news.models import News
from posts.models import Post

import random
# Create your views here.


# @login_required(login_url='login_page')
def user_profile(request, usrname): #HINT: LOOK FOR MAL OR ANILIST
    user = User.objects.get(username=usrname)
    follow = None
    logged_in = request.user.is_authenticated
    my_profile = user == request.user
    designation = user.designation
    all_news = News.objects.all().filter(posted_by=user, is_approved=True)
    all_posts = Post.objects.all().filter(posted_by=user)

    # Primary check for follow
    if request.user.is_authenticated:
        try:
            follow = Followings.objects.get(user_id=request.user, following_user_id=user)
        except ObjectDoesNotExist:
            follow = None
    
    context = {
        'user': user,
        'designation': designation,
        'all_news': all_news,
        'all_posts': all_posts,
        'my_profile': my_profile,
        'follow': follow,
        'logged_in': logged_in,
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