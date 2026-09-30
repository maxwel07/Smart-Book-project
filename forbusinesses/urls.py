from django.urls import path
from .views import for_businesses


urlpatterns = [
    path('', for_businesses, name="for_businesses")
]