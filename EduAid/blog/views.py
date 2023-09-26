from django.shortcuts import render
from django.views import generic
from rest_framework import generics

# from rest_framework.generics import ListAPIView
from .models import Blog, ResourceUploader
from .serializer import Blog_Serializer, Resource_serializer

# Create your views here


# For Blog Portion


class View_Blog(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = Blog_Serializer


class Create_Blog(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = Blog_Serializer


class Upadate_Blog(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = Blog_Serializer


class Detail_Blog(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = Blog_Serializer


# For Resource Uploader


class Create_Resource(generics.CreateAPIView):
    queryset = ResourceUploader.objects.all()
    serializer_class = Resource_serializer


class Update_Resource(generics.UpdateAPIView):
    queryset = ResourceUploader.objects.all()
    serializer_class = Resource_serializer


class Delete_Resource(generics.DestroyAPIView):
    queryset = ResourceUploader.objects.all()
    serializer_class = Resource_serializer
