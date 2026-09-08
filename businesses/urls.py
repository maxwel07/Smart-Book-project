from django.urls import path
from .views import business

urlpatterns = [
    path('businesses/', business, name='business_page' )
]