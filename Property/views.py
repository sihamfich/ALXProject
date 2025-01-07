from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Property



# Create your views here.
class PropertyListView(ListView):
    model = Property 
    # filtering the queryset
    # pagination
class PropertyDetailView(DetailView):
    model = Property
    # Booking
