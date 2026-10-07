from django.shortcuts import render, redirect
from .forms import registerForm
from django.contrib.auth import authenticate, login

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

def login(request):
    pass