from django.shortcuts import render


# Create your views here.
def how_it_works(request):
    return render(request, 'how_it_works.html')