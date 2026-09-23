from django.shortcuts import render, redirect, get_object_or_404
from .models import Business
from .forms import ReviewForm

# Create your views here.
def business(request):
    businesses = Business.objects.all()
    context = {
        'businesses': businesses
    }
    return render(request, 'businesses.html', context)



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
        review_form = ReviewForm()

    context = {
        'business': business,
        'services': services,
        'images': images,
        'reviews': reviews,
        'review_form': review_form
    }
    return render(request, 'business_detail.html', context)     

