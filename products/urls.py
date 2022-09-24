from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllProductsView, name='products'),
    path('<int:product_id>/', views.ProductDetail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
]