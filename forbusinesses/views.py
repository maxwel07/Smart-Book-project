from django.shortcuts import render


# Create your views here.
def for_businesses(request):
    return render(request, 'for_businesses.html')