from django.urls import path
from .views import home , home_search, CategoryFilter, ContactUs

app_name = 'Settings'

urlpatterns = [

    path('', home, name='home'),
    path('search/', home_search, name='home_search'),
    path('contact_us/', ContactUs, name='ContactUs'),
    path('category/<slug:category>', CategoryFilter, name='category_filter')
]