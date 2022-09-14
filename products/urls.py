from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllProductsView, name='products'),
    path('<product_id>', views.ProductDetail, name='product_detail'),
]