from django.urls import path
from .views import PropertyListView, PropertyDetailView 
from .api_view import PropertyAPIList, PropertyAPIDetail

app_name = 'Property'

urlpatterns = [
    path('', PropertyListView.as_view(), name='property_list'),
    path('<slug:slug>/', PropertyDetailView.as_view(), name='property_detail'),
    
    path('api/list', PropertyAPIList.as_view(), name='property_api_list'),
    path('api/list/<int:pk>', PropertyAPIDetail.as_view(), name='property_api_detail'),
]
