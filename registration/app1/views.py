
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.model import user
from .forms import CustomUserCreationForm



# Create your views here.

def HomePage(request):
    return render (request, 'home.html')

# appname/views.py


def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def LoginPage(request):
    return render (request, 'login.html')
