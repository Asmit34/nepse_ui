from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from .forms import SignUpForm
from .models import User, Profile
from django.contrib.auth.decorators import login_required


def SignUpView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "You have signed up successfully!")
            return redirect('signin')
        else:
            messages.error(request, "There were some errors with your submission.")
    else:
        form = SignUpForm()
    return render(request, "users/signup.html", {'form': form})

def SignInView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "You have logged in successfully!")
            return redirect('index')  # Redirect to 'index' after login
        else:
            messages.error(request, "Unable to login! Please check your credentials.")
    return render(request, "users/signin.html")

def LogoutView(request):
    logout(request)
    messages.success(request, "You have logged out successfully!")
    return redirect('signin')

# Adding the index view
def index(request):
    return render(request, "users/index.html")

@login_required
def profile_view(request, user_id):
    profile = Profile.objects.get(user__id=user_id)
    return render(request, "users/profile.html", {'profile': profile})
