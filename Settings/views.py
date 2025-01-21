from django.shortcuts import render
from Property.models import Property , Location, Category
from django.db.models import Count
from django.db.models.query_utils import Q

# Create your views here.

def home(request):
    locations = Location.objects.all().annotate(property_count=Count('Property_Location'))
    category = Category.objects.all()
    
    resturant_list = Property.objects.filter(Category__Name='Restaurant')[:4]
    hotel_list = Property.objects.filter(Category__Name='Hotel')[:3]
    location_list = Property.objects.filter(Category__Name='Place')[:3]
    
    return render(request, 'Settings/home.html', {
        'locations': locations,
        'category': category,
        'resturant_list': resturant_list,
        'hotels_list': hotel_list,
        'location_list': location_list,
    })


def home_search(request):
    name = request.GET.get('name')
    location = request.GET.get('location')

    property_list = Property.objects.filter(
        Q(Name__icontains=name) &
        Q(Location__Name__icontains=location)
    )
    
    return render(request,'Settings/home_search.html', {'property_list': property_list})

def CategoryFilter(request, category):
    category = Category.objects.get(Name=category)
    property_list = Property.objects.filter(Category=category)
    return render(request, 'Settings/home_search.html', {'property_list': property_list})