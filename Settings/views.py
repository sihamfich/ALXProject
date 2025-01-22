from django.shortcuts import render
from Property.models import Property , Location, Category
from django.db.models import Count
from django.db.models.query_utils import Q
from Blog.models import BlogPost
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    locations = Location.objects.all().annotate(property_count=Count('Property_Location'))
    category = Category.objects.all()
    
    resturant_list = Property.objects.filter(Category__Name='Restaurant')[:4]
    hotel_list = Property.objects.filter(Category__Name='Hotel')[:3]
    location_list = Property.objects.filter(Category__Name='Place')[:3]
    
    recent_blogpost = BlogPost.objects.all()[:4]
    users_count = User.objects.all().count()
    places_count = Property.objects.filter(Category__Name='Place').count()
    hotel_count = Property.objects.filter(Category__Name='Hotel').count()
    restaurant_count = Property.objects.filter(Category__Name='Restaurant').count()
    
    return render(request, 'Settings/home.html', {
        'locations': locations,
        'category': category,
        'resturant_list': resturant_list,
        'hotels_list': hotel_list,
        'location_list': location_list,
        'recent_blogpost': recent_blogpost,
        'users_count': users_count,
        'places_count': places_count,
        'hotel_count': hotel_count,
        'restaurant_count': restaurant_count
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

def ContactUs(request):
    pass