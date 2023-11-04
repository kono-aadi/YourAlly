from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required
def HomePage(request):
    return render(request, 'auth_system/index.html', {})

def HomePage(request):
    return render(request, 'auth_system/index.html', {})

def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('sname')
        name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        if len(password) < 4:
            messages.error(request, 'Password must be at least 4 characters')
            return redirect('register-page')

        new_user = User.objects.create_user(name, email, password)
        new_user.first_name = fname
        new_user.last_name = lname

        new_user.save()
        return redirect('login-page')
    return render(request, 'auth_system/register.html', {})

def Login(request):
     if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            messages.error(request, 'username and/or password is incorrect')
            return redirect('login-page')

     return render(request, 'auth_system/login.html', {})

def logoutuser(request):
    logout(request)
    return redirect('login-page')

def test(request):
    return render(request, 'auth_system/test.html', {})