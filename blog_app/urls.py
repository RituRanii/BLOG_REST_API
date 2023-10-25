from django.urls import path, include
from .import views

urlpatterns = [
    path("blog_list/",views.BlogListCreateView.as_view(), name = "blog_list"),
    path("blog_detail/<int:pk>/",views.BlogDetailView.as_view(),name="blog_list_view"),
    path("category_list/",views.CategoryListeCreateView.as_view(),name="category_list_view"),
    path("category_detail/<int:pk>",views.CategorydetailView.as_view(),name="category_detail_view"),
    path("blog_comment_list/<int:blog_id>/",views.BlogCommentListCreateView.as_view(),name="blog_comment_list"),
]