from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    # #class based view urls
    # #path('class_blog_list/', views.BlogListView.as_view(),name="all_blog_list"),
    # path('class_blog_details/<int:pk>/', views.BlogDetailView.as_view(),name="blog_detail"),
    # #category URLS
    # path('Category_list/', views.CategoryListView.as_view(), name="category_list"),
    # path('Category_detail/<int:pk>/', views.CategoryDetailView.as_view(), name="category-detail"),
    # #generic view lists
    # path('blog_list_generic_view/', views.BlogListGenericView.as_view(), name="blog_list_generic_view"),
    # path('blog_detail_generic_view/<str:slug>/', views.BlogDetailGenericView.as_view(), name="blog_detail_generic_view"),

    path('blog_create_createapiview/',views.BlogCreateConc.as_view(), name ="blog_create_createapiview"),
    path('blog_list_listapiview/',views.BlogListcon.as_view(), name ="blog_list_createapiview"),
    path('blog_retrieve_retrieveapiview/<str:slug>/',views.BlogRetrievecon.as_view(), name ="blog_retrieve_retrieveapiview"),
    path('blog_destroyapiview/<int:pk>/',views.BlogDestroycon.as_view(), name = 'blog_destroy_destroyapiview'),
    path('blog_Updateapiview/<int:pk>/',views.BlogUpdatecon.as_view(), name = 'blog_Updateapiview'),
    path('blog_retrieveUpdateapiview/<int:pk>/',views.BlogretrieveUpdatecon.as_view(), name = 'blog_retrieveUpdate_retrieveUpdateapiview'),
    path('blog_retrievedestroyapiview/<int:pk>/',views.BlogRetrieveDestrouconc.as_view(), name = 'blog_retrievedestroy_retrievedestroyapiview'),
] 