from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from app.models import *

# Create your views here.
def Login(request):
    form = LoginUserForm()
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user:
                login(request,user)
                messages.success(request, f'Hey {username}, you have successfully logged in ')
                return redirect('home')
            else:
                messages.error(request, 'Please Enter the correct login details')
        else:
            messages.error(request, 'Unable to login')
    context={
        'form':form,
    }
    return render(request, 'registration/login.html', context)

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hey {username}, you have successfully created your account ')
            return redirect('login')
    else:
        form = SignupForm()

    context ={
        'form':form,
    }


    return render(request, 'registration/register.html', context)

def Logout(request):
    logout(request)
    return redirect('login')

def profile(request):
    foods = Food.objects.all()
    context={
        'foods':foods,
    }
    return render(request, 'pages/profile.html',context)

def change_password(request):
    foods = Food.objects.all()
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) #to keep the user logged in
            return redirect('change_password_done')
    else:
        form = PasswordChangeForm(request.user)
        
    context={
        'form':form,
        'foods':foods,
    }

    return render(request, 'registration/change_password.html', context)
    

def change_password_done(request):
     foods = Food.objects.all()
     context={
        'foods':foods,
    }
     return render(request, 'registration/change_password_done.html', context)