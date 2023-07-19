from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'account/profile.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('documentary_list')
        else:
            return render(request, 'account/login.html', {'error': 'Invalid username or password.'})
    return render(request, 'account/login.html')

def user_signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, password=password)
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'account/signup.html', {'form': form})
