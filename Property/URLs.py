from django.urls import path
from .views import PropertyListView, PropertyDetailView 

AppName = 'Property'

urlpatterns = [
    path('', PropertyListView.as_view(), name='property-list'),
    #path('', PropertyDetailView.as_view(), name='property-detail'),
]