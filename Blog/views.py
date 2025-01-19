from django.shortcuts import render
from taggit.models import Tag
from django.views.generic import ListView, DetailView
from .models import BlogPost, Category
from django.db.models import Count, Q

# Create your views here.
class PostList(ListView):
    model = BlogPost
    paginate_by = 2
    
    def get_queryset(self):
        name=self.request.GET.get('q', '')
        object_list = BlogPost.objects.filter(
            Q(Title__icontains=name) | Q(Description__icontains=name)
        )
        return object_list

class PostDetail(DetailView):
    model = BlogPost

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all().annotate(num_posts=Count('BlogPost_Category'))
        context['tags'] = Tag.objects.all()
        context['recent_posts'] = BlogPost.objects.all().order_by('-CreatedDate')[:3]
        return context
        
class FilterByCategory(ListView):
    model = BlogPost
    
    def get_queryset(self):
        slug=self.kwargs['slug']
        object_list = BlogPost.objects.filter(
            Q(Category__Name__icontains=slug)
        )   
        return object_list
    
class FilterByTags(ListView):
    model = BlogPost
    
    def get_queryset(self):
        slug=self.kwargs['slug']
        object_list = BlogPost.objects.filter(
            Q(Tags__name__icontains=slug) # Use 'tags__name' for django-taggit
        )
        return object_list