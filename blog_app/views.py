from django.shortcuts import render
from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Blog, Category
from rest_framework import status
from rest_framework import mixins, generics

# class CategoryListView(APIView):
#     def get(self, request):
#         all_category = Category.objects.all()
#         serializers = CategorySerializer(all_category, many=True, context={'request': request})
#         return Response(data=serializers.data)
    
# class CategoryDetailView(APIView):
#     def get(self, request, pk):
#         single_category = Category.objects.get(pk=pk)
#         serializers = CategorySerializer(single_category, context={'request': request})
#         return Response(data=serializers.data)
# # generic view
# class BlogListGenericView(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# #GET,PUT,DELETE
# class BlogDetailView(APIView):
#     def get(self,request,pk):
#         blog = Blog.objects.get(is_public=True, pk=pk)
#         serializer = BlogSerializer(blog)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     def put(self,request,pk):
#         blog = Blog.objects.get(pk=pk)
#         serializer = BlogSerializer(blog,data=request.data)
#         if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self,requesr,pk):
#         blog = Blog.objects.get(pk=pk)
#         blog.delete()
#         return Response(status=status.HTTP_200_OK)

# class BlogDetailGenericView(mixins.RetrieveModelMixin,
#                             mixins.UpdateModelMixin,
#                             mixins.DestroyModelMixin,
#                             generics.GenericAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#     lookup_field = 'slug' 

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)    

# Concrete View Classes
class BlogCreateConc(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
class BlogListcon(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
class BlogRetrievecon(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'slug'
class BlogDestroycon(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
class BlogUpdatecon(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
class BlogretrieveUpdatecon(generics.RetrieveUpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
class BlogRetrieveDestrouconc(generics.RetrieveDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    

    

       
      

    
