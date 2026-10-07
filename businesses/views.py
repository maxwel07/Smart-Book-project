from django.shortcuts import render, redirect, get_object_or_404
from .models import Business
from .forms import ReviewForm
from datetime import datetime
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def business(request):
    search = request.GET.get('search')
    location = request.GET.get('location')
    categories = request.GET.getlist('category')
    price_range = request.GET.get('price_range')
    rating = request.GET.get('rating')
    sort = request.GET.get('sort')
    open_now = request.GET.get('open_now')
    query_params = request.GET.copy()
    query_params.pop('page', None)
    query_string = query_params.urlencode()

    businesses = Business.objects.all()

    if categories:
        businesses = businesses.filter(category__in=categories)

    if search:
        businesses = businesses.filter(
            Q(name__icontains=search) | Q(services__name__icontains=search)
        ).distinct()

    if location:
        businesses = businesses.filter(location__icontains = location)

    if price_range:
        businesses = businesses.filter(price_range=price_range)

    if rating:
        businesses = businesses.filter(rating__gte=rating)

    if open_now:
            current_time = datetime.now().time()
            businesses = businesses.filter(
                opening_time__lte = current_time,
                closing_time__gte = current_time
            )

    if sort == 'rating':
        businesses = businesses.order_by('-rating')

    elif sort == 'price_low':
        businesses = businesses.order_by('price_range')

    elif sort == 'price_high':
        businesses = businesses.order_by('-price_range')

    

    paginator = Paginator(businesses, 6)
    page_number = request.GET.get('page')
    businesses = paginator.get_page(page_number)

    context = {
        'businesses': businesses,
        'query_string': query_string
    }
    print("QUERY STRING:", query_string)
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

 

