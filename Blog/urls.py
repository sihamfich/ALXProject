from django.urls import path
from . import views
from .api_view import post_list_api, post_detail_api, post_search_api


app_name = 'Blog'
urlpatterns = [
    path('', views.PostList.as_view(), name='blogpost_list'),
    path('<slug:slug>', views.PostDetail.as_view(), name='blogpost_Detail'),
    
    path('category/<str:slug>', views.FilterByCategory.as_view(), name='filter_by_category'),
    path('tags/<str:slug>', views.FilterByTags.as_view(), name='filter_by_tags'),
    
    ## API URL
    path('api/list', post_list_api, name='post_list_api'),
    path('api/list/<int:id>', post_detail_api, name='post_detail_api'),
    path('api/list/search/<str:query>', post_search_api, name='post_search_api'),
]
