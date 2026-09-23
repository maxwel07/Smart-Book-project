from django.urls import path
from .views import business, business_detail

urlpatterns = [
    path('', business, name='business_list' ),
    path('<int:business_id>/', business_detail, name='business_detail'),
   # path('success/', success, name='success')
]