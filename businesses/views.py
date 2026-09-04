from django.shortcuts import render

# Create your views here.
def business(request):
    return render(request, 'businesses.html')