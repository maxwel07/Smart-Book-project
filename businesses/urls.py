from django.urls import path
from .views import business, business_detail

urlpatterns = [
    path('', business, name='business_list' ),
    path('<int:business_id>/', business_detail, name='business_detail'),
<<<<<<< HEAD
   # path('success/', success, name='success')
=======
>>>>>>> 98bcece778846efd2d4b61364bb38fdb7dcdc270
]