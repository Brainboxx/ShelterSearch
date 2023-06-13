from django.urls import path
from .views import PropertyListView, PropertyDetailView, PropertySearchView

urlpatterns = [
    path('', PropertyListView.as_view(), name='properties'),
    path('property/<int:pk>', PropertyDetailView.as_view(), name='property-detail'),
    path('search/', PropertySearchView.as_view(), name='search')
]