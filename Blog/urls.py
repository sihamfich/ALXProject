from django.urls import path
from . import views


app_name = 'Blog'
urlpatterns = [
    path('', views.PostList.as_view(), name='blogpost_list'),
    path('<slug:slug>', views.PostDetail.as_view(), name='blogpost_Detail'),
    
    path('category/<str:slug>', views.FilterByCategory.as_view(), name='filter_by_category'),
    path('tags/<str:slug>', views.FilterByTags.as_view(), name='filter_by_tags'),
]
