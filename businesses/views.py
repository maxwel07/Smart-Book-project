from django.shortcuts import render,get_object_or_404
from .models import Business

# Create your views here.
def business(request):
    businesses = Business.objects.all()
    return render(request, 'businesses.html',{'businesses':businesses})



def business_detail(request, business_id):
    business = get_object_or_404(Business, id=business_id)  
    services = business.services.filter(is_active=True)
    images = business.images.all()
    reviews = business.reviews.all()
    
    return render(request, 'business_detail.html', {'business':business, 
                                                    'images':images, 
                                                    'services':services, 
                                                    'reviews':reviews})        
