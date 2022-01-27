from django.shortcuts import render, redirect
from .models import Profile

from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .forms import CustomUserCreationForm

# Create your views here.

def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'Username does not exist.')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username OR Password incorrect.')

    context = {'page':page}
    return render(request, 'users/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User account created successfully!')
            login(request, user)
            return redirect('profiles')

        else:
            messages.success(request, 'An error occured while registration.')

    context = {'page':page, 'form':form}
    return render(request, 'users/login_register.html', context)


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles' : profiles}
    return render(request, "users/profiles.html", context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    topskills = profile.skill_set.exclude(description__exact = "")
    otherskills = profile.skill_set.filter(description = "")
    context = { 'profile' : profile, 'topskills' : topskills, 'otherskills' : otherskills }
    return render(request, 'users/user-profile.html', context)