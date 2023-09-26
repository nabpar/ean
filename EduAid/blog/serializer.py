from rest_framework import serializers

from .models import Blog, ResourceUploader

# class BlogView_Serializer(serializers.ModelSerializer):
#     title = serializers.TextField(max_length=255)

#     class Meta:
#         models = Blog
#         fields =


class Blog_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class Resource_serializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceUploader
        fields = ["comment"]
