from django.urls import path
from . import views
from .api_view import PropertyAPIList, PropertyAPIDetail

app_name = 'Property'

urlpatterns = [
    path('', views.PropertyListView.as_view(), name='property_list'),
    path('new', views.NewProperty.as_view(), name='property_new'),
    path('<slug:slug>/', views.PropertyDetailView.as_view(), name='property_detail'),
    path('category/<str:category>', views.property_category_view, name='filter_category'),

    path('api/list', PropertyAPIList.as_view(), name='property_api_list'),
    path('api/list/<int:pk>', PropertyAPIDetail.as_view(), name='property_api_detail'),
    
]
