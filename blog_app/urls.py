from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    #class based view urls
    #path('class_blog_list/', views.BlogListView.as_view(),name="all_blog_list"),
    path('class_blog_details/<int:pk>/', views.BlogDetailView.as_view(),name="blog_detail"),
    #category URLS
    path('Category_list/', views.CategoryListView.as_view(), name="category_list"),
    path('Category_detail/<int:pk>/', views.CategoryDetailView.as_view(), name="category-detail"),
    #generic view lists
    path('blog_list_generic_view/', views.BlogListGenericView.as_view(), name="blog_list_generic_view"),
    path('blog_detail_generic_view/<int:pk>/', views.BlogDetailGenericView.as_view(), name="blog_detail_generic_view"),
]