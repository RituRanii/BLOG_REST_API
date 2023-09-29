from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('blog_list/',views.blog_list,name="blog_list"),
    path('blog_details/<int:pk>/',views.blog_details,name="blog_details"),
]