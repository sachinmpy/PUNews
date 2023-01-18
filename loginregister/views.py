from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, UserLoginForm


def login_page(request):
    form = UserLoginForm()

    if request.method == 'POST':
        username = request.POST['username']
        # email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'WELCOME!!')
            return redirect('/')

    context = {'form': form}
    return render(request, 'loginregister/login_page.html', context)


def register_page(request):

    form = UserRegisterForm()

    if request.method == 'POST':
        # print(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username'].upper()
            user.set_password(
                form.cleaned_data['password']
            )
            user.save() 
            messages.success(request,  f'{username} ACCOUNT HAS BEEN CREATED')
            return redirect('/login/')
        else:
            pass #HANDLE THIS FOR FUCK SAKE

    context = {
        'form': form,
    }
    return render(request, 'loginregister/register_page.html', context)

def logout_user(request):
    logout(request)
    return redirect('/')