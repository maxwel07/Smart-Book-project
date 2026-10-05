from django.shortcuts import render, redirect, get_object_or_404
from .models import Business
from .forms import ReviewForm
from datetime import datetime

# Create your views here.
def business(request):
    search = request.GET.get('search')
    location = request.GET.get('location')
    categories = request.GET.getlist('category')
    price_range = request.GET.get('price_range')
    rating = request.GET.get('rating')
    sort = request.GET.get('sort')
    print('SORT:', sort)
    open_now = request.GET.get('open_now')
    businesses = Business.objects.all()

    if categories:
        businesses = businesses.filter(category__in=categories)

    if search:
        businesses = businesses.filter(name__icontains = search)

    if location:
        businesses = businesses.filter(location__icontains = location)

    if price_range:
        businesses = businesses.filter(price_range=price_range)

    if rating:
        businesses = businesses.filter(rating__gte=rating)

    if sort == 'rating':
        businesses = businesses.order_by('-rating')

    elif sort == 'price_low':
        businesses = businesses.order_by('price_range')

    elif sort == 'price_high':
        businesses = businesses.order_by('-price_range')

    
    if open_now:
        current_time = datetime.now().time()
        businesses = businesses.filter(
            opening_time__lte = current_time,
            closing_time__gte = current_time
        )
        

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

 

