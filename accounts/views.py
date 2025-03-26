from django.shortcuts import render, redirect 
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login

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
            print(form.get_user())
            auth_login(request, form.get_user())
            return redirect('articles:index')

    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'login.html', context)