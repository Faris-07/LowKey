from django.urls import path
from . import views

urlpatterns = [
    path('', views.BagView, name='bag_view'),
    path('add/<item_id>/', views.AddToBag, name='add_to_bag'),
]