from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from user_models.models import User

# Create your views here.

# @login_required(login_url='login_page')
def user_profile(request, usrname): #HINT: LOOK FOR MAL OR ANILIST
    user = User.objects.get(username=usrname)
    designation = user.designation
    context = {
        'user': user,
        'designation': designation,

    }
    return render(request, 'user_models/user_profile.html', context)

    #NEEDS TO IMPLEMENT PROFILE SETTING


@login_required(login_url='login_page')
def user_settings(request, username):
    return HttpResponse(f"{username}")


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