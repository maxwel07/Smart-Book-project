from django.urls import path
from . import views

urlpatterns = [
    path('', views.business, name='business_list' ),
    path('<int:business_id>/book/', views.create_booking, name='create_booking'),
    path('<int:business_id>/', views.business_detail, name='business_detail'),
]