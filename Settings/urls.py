from django.urls import path
from .views import home , home_search

app_name = 'Settings'

urlpatterns = [

    path('', home, name='home'),
    path('search/', home_search, name='home_search'),
]