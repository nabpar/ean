from .models import Category,Subject,Syllabus
from rest_framework import serializers
from .file_upload import Uploader

# Category Serialization

class Search_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        ref_name = 'CategorySearch'



class Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



# subject Serialization

class Subject_Serializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    def get_category_name(self,obj):
        return obj.category.name


    class Meta:
        model = Subject
        fields = '__all__'


# #Topic Serialization

# class Topic_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model =  Topic
#         fields = '__all__' 

# # Subtopic serializer        

# class Subtopic_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subtopic
#         fields = '__all__' 

# Syllabus Serializer
class Syllabus_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Syllabus
        fields = '__all__'        




 # Uploader serializer 

class Uploader_serializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    subject_name = serializers.SerializerMethodField()

    def get_category_name(self,obj):
        return obj.category.name
    
    def get_subject_name(self,obj):
        return obj.subject.name
    class Meta:
        model = Uploader
        fields = '__all__'