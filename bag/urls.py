from django.urls import path
from . import views

urlpatterns = [
    path('', views.BagView, name='bag_view'),
]