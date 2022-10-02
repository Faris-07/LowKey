from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.apply_coupon, name='apply_coupon'),
    path('add/', views.add_coupon, name='add_coupon'),
]
