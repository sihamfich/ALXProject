from django.shortcuts import render
from Property.models import Property , Location
from django.db.models import Count, Q

# Create your views here.

def home(request):
    locations = Location.objects.all()
    
    return render(request, 'Settings/home.html', {
        'locations': locations
    })


def home_search(request):
    name = request.GET.get('name')
    location = request.GET.get('location')

    property_list = Property.objects.filter(
        Q(Name__icontains=name) &
        Q(Location__Name__icontains=location)
    )
    
    return render(request, 'Settings/home_search.html', {'property_list': property_list})