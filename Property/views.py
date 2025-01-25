from django.db.models.base import django
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView
from .models import Property, Category, PropertyReview, PropertyImages
from django.views.generic.edit import FormMixin
from .Forms import PropertyBookingForm
from .filters import PropertyFilter
from django_filters.views import FilterView
from django.contrib import messages
from django.urls import reverse

# Create your views here.
class PropertyListView(FilterView):
    model = Property 
    # pagination
    paginate_by = 3
    filterset_class = PropertyFilter
    template_name = 'Property/property_list.html'
    
class PropertyDetailView(FormMixin, DetailView):
    model = Property  
    form_class = PropertyBookingForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related'] = Property.objects.filter(Category=self.get_object().Category)[:2]
        context['Review_count'] = PropertyReview.objects.filter(Property=self.get_object()).count()
        context['property_images'] = PropertyImages.objects.filter(Property=self.get_object().id)
        return context  
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.Property = self.get_object()
            myform.User = request.user
            myform.save()
            messages.success(request, 'Your Reservation Confirmed ')
            
            return redirect(reverse('Property:property_detail' , kwargs={'slug':self.get_object().slug}))
        

class NewProperty(CreateView):
    model = Property
    fields = ['Name', 'Description', 'Price', 'Location', 'Main_Image', 'Category']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            messages.success(request, 'Successfully Added Your Property')

            ### send gmail message
            return redirect(reverse('Property:property_list'))


def property_category_view(request, category):
    my_category = Category.objects.get(Name=category)
    properties = Property.objects.filter(Category=my_category)
    return render(request, 'Property/filter_category.html', {'properties': properties, 'my_category': my_category})