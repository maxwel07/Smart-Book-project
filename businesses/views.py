from django.shortcuts import render
from .models import Business

# Create your views here.
def business(request):
    businesses = Business.objects.all()
    return render(request, 'businesses.html',{'businesses':businesses})
                  