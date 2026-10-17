from django.shortcuts import render, redirect
from .forms import registerForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = registerForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)   


        if user is not None:
            login(request, user)

            return redirect('home')

        messages.error(request, 'Invalid username or password. Please check your details or create an account.') 

    return render(request, 'accounts/login.html')

@require_POST
def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def my_account(request):
    return render(request, 'accounts/my-account.html', {
        'user': request.user
    })