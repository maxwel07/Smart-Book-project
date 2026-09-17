from django.shortcuts import render,get_object_or_404, redirect
from .models import Business
from .forms import ReviewForm

# Create your views here.
def business(request):
    businesses = Business.objects.all()
    return render(request, 'businesses.html',{'businesses':businesses})



def business_detail(request, business_id):
    business = get_object_or_404(Business, id=business_id)  
    services = business.services.filter(is_active=True)
    images = business.images.all()
    reviews = business.reviews.all()
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.business = business
            review.save()
            return redirect('business_detail', business_id=business.id)
        else:
            print(review_form.errors)
    else:
        review_form = ReviewForm()

    return render(request, 'business_detail.html', {'business':business, 
                                                    'images':images, 
                                                    'services':services, 
                                                    'reviews':reviews,
                                                    'review_form': review_form})        
