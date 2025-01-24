from django.urls import path
from . import views
from .api_view import PropertyAPIList, PropertyAPIDetail

app_name = 'Property'

urlpatterns = [
    path('', views.PropertyListView.as_view(), name='property_list'),
    path('<slug:slug>', views.PropertyDetailView.as_view(), name='property_detail'),
    path( 'new', views.NewProperty.as_view() , name='property_new'),
    path('category/<str:category>',views.Property_Category , name='filter_category'),
    
    path('api/list', PropertyAPIList.as_view(), name='property_api_list'),
    path('api/list/<int:pk>', PropertyAPIDetail.as_view(), name='property_api_detail'),
    
]
