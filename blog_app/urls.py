from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    # path('blog_list/',views.blog_list,name="blog_list"),
    # path('blog_details/<int:pk>/',views.blog_details,name="blog_details"),
    #class based view urls
    path('class_blog_list/', views.BlogListView.as_view(),name="all_blog_list"),
    path('class_blog_details/<int:pk>/', views.BlogDetailView.as_view(),name="blog_detail"),
]