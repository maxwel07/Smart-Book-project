from django.shortcuts import render
from businesses.models import Business

def home (request):
    featured_businesses = Business.objects.all()[:4]
    context = {
        'businesses': featured_businesses
    }
    return render(request, 'core/home.html', context)


