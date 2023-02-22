from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from flask import Flask

# Create your views here.
def register(request):
    app = Flask(__name__)
    print(app)
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'Account Created for {username}')
            form.save()
            return redirect('login')

    else:
        form = UserRegistrationForm()

    form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):

    return render(request, 'users/profile.html')