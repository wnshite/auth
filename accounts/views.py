from django.shortcuts import render, redirect 
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import User

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'signup.html', context)

def login(request):
    if request.method =='POST': 
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())

            # /accounts/login/ -> next 가 없는 경우(none이 들어옴), .get은 none을 반환.
            # /accounts/login/?next=/articles/create/ -> next 가 있는 경우
            next_url = request.GET.get('next')

            # next가 없는 경우 -> None or 'articles:index'
            # next가 있을 경우 -> 'articles/create' or 'articles:index'
            return redirect(next_url or 'articles:index')

    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')
    
def profile(request, username):
    user_profile = User.objects.get(username=username)
    
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'profile.html', context)