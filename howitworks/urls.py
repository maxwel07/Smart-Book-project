from django.urls import path
from .views import how_it_works

urlpatterns = [
    path('', how_it_works, name='how_it_works')
]