from django.db.models import Q,Case, When, Value, IntegerField
from django.db.models.functions import Length
from itertools import chain
from operator import itemgetter
from rest_framework.response import Response
from rest_framework import status


from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from  rest_framework import generics
from .serializer import Category_Serializer,Subject_Serializer,Syllabus_Serializer,Search_Serializer,Uploader_serializer
from .models import Category,Subject,Syllabus
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.viewsets import ModelViewSet
from .file_upload import Uploader
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer

# Create your views here.

#Fro searching the category
class SearchCategory(generics.ListAPIView):
    queryset =Category.objects.all()
    serializer_class = Search_Serializer
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ['^name','name']
    OrderingFilter = ['name']
    # def get_queryset(self):
    #     queryset = super(SearchCategory, self).get_queryset()
    #     search_term = self.request.query_params.get('search', None)
    #     if search_term:
    #         starts_with_results = queryset.filter(name__istartswith=search_term)
    #         contains_results = queryset.filter(name__icontains=search_term)

    #         # Combine the QuerySets using chain()
    #         combined_results = list(starts_with_results) + list(contains_results)

    #         # Sort the combined results based on the proximity of the search term within the names
    #         sorted_results = sorted(
    #             combined_results,
    #             key=lambda x: (x.name.startswith(search_term), x.name.find(search_term))
    #         )

    #         return sorted_results

    #     return queryset



    # def get_queryset(self):
    #     queryset = super(SearchCategory, self).get_queryset()
    #     search_term = self.request.query_params.get('search', None)
    #     if search_term:
    #         starts_with_results = queryset.filter(name__istartswith=search_term)
    #         contains_results = queryset.filter(name__icontains=search_term)

    #         # Calculate relevance score based on the length of the prefix matching the search term
    #         relevance_score = Case(
    #             When(name__istartswith=search_term, then=Length('name')),
    #             When(name__icontains=search_term, then=Value(1000) - Length('name')),
    #             default=Value(0),
    #             output_field=IntegerField()
    #         )

    #         # Combine the QuerySets using union() and annotate the relevance score
    #         combined_results = starts_with_results.union(contains_results).annotate(relevance=relevance_score)

    #         # Order the results based on the relevance score in ascending order
    #         sorted_results = combined_results.order_by('relevance')

    #         return sorted_results

    #     return queryset
    
    # def get_queryset(self):
    #     queryset = super(SearchCategory,self).get_queryset()
    #     search_term  = self.request.query_params.get('search',None)
    #     if search_term:
    #         starts_with_results = queryset.filter(name__istartswith=search_term)
    #         contains_results = queryset.filter(name__icontains = search_term)

    #         # combined_results = list(starts_with_results) + list(contains_results)
    #         # combined_results = (starts_with_results | contains_results).distinct()


    #         sorted_results = list(sorted(chain(starts_with_results,contains_results),key=lambda x: x.name.find(search_term)))
    #         return sorted_results
    #     return queryset



    # def get_queryset(self):
    #     return super().get_queryset.filter(name__icontains='name')
        # return Category.objects.filter(data_from_category = data)

    # ordering_fields = ['=name']
    # def services(request):
    #     queryset = Category.objects.all()
    #     if request.method  == "GET":
    #         st = request.GET.get('name')
    #         if st!=None:
    #             queryset = Category.objects.filter(category_title__icontains=st)

    #             data = {
    #                 'queryset':queryset
    #             }
    #             return request.data



class Create_Category_View(generics.CreateAPIView):
    queryset= Category.objects.all()
    serializer_class = Category_Serializer



class List_Category_view(generics.ListAPIView):
    queryset= Category.objects.all()
    serializer_class = Category_Serializer
    # filter_backends = (SearchFilter)
    # search_fields = ["name"]


    # def filter(request):
    #     filter_data = BaseClass.objects.all()
    #     if request.method =="GET":
    #         fd = request.GET.get("name")
    #         if fd!= None :
    #             filter_data = filter.objects.filter(cat_name=fd)
    #     return request(filter_data)

class Update_Category_View(generics.UpdateAPIView):
    queryset = Category.objects.all()    
    serializer_class = Category_Serializer

class Delete_Category_View(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class =Category_Serializer

# For Subject
class Create_Subject_View(generics.CreateAPIView):

    queryset= Subject.objects.all()
    serializer_class = Subject_Serializer

class List_Subject_view(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = Subject_Serializer
    filterset_fields = ('category','name')

    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'my_template.html'

    # def get(self,request):
    #     queryset = Subject.objects.all()
    #     serializer= Subject_Serializer(queryset,many = True)
    #     return Response({'data':serializer.data})

        

    # def get_queryset(self,request,category_id):
    #     category = get_object_or_404(Category,pk=category_id)
    #     subjects = Subject.objects.filter(category=category)

    #     return super().get_queryset()

    # def Subject_List(request,category_id):
    #     category= get_object_or_404(Category,pk=category_id)
    #     subject = Subject.objects.filter(categoy=category)
    #     return render(request,{'category':category,  'subject':subject})
    # def get_queryset(self):
    #     category_id = self.request.query_params.get('category')
    #     queryset = Subject.objects.all()
    #     if category_id:
    #         queryset = queryset.filter(subject__category_id=category_id)

    #     return queryset
    # def get(self,request,*args,**kwargs):
    #     queryset= self.get_queryset()
    #     serializer = Subject_Serializer(queryset,many=True)
    #     return Response(serializer.data,status = status.HTTP_200_OK)    


class Update_Subject_View(generics.UpdateAPIView):
    queryset = Subject.objects.all()    
    serializer_class = Subject_Serializer

class Delete_Subject_View(generics.DestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = Subject_Serializer






# # For Topic

# class Create_Topic_View(generics.CreateAPIView):
#     queryset= Subject.objects.all()
#     serializer_class = Syllabus_Serializer

# class List_Topic_view(generics.ListAPIView):
#     queryset= Topic.objects.all()
#     serializer_class = Syllabus_Serializer

# class Update_Topic_View(generics.UpdateAPIView):
#     queryset = Topic.objects.all()    
#     serializer_class = Syllabus_Serializer

# class Delete_Topic_View(generics.DestroyAPIView):
#     queryset = Topic.objects.all()
#     serializer_class = Syllabus_Serializer

# # For Sub_Topic

# class Create_Subtopic_View(generics.CreateAPIView):
#     queryset= Subtopic.objects.all()
#     serializer_class = Subtopic_Serializer

# class List_Subtopic_view(generics.ListAPIView):
#     queryset= Subtopic.objects.all()
#     serializer_class =Subtopic_Serializer

# class Update_Subtopic_View(generics.UpdateAPIView):
#     queryset = Subtopic.objects.all()    
#     serializer_class = Subtopic_Serializer

# class Delete_Subtopic_View(generics.DestroyAPIView):
#     queryset = Subtopic.objects.all()
#     serializer_class = Subtopic_Serializer


# For Syllabus


class Create_Syllabus_View(generics.CreateAPIView):
    queryset= Syllabus.objects.all()
    serializer_class = Syllabus_Serializer

class List_Syllabus_view(generics.ListAPIView):
    queryset= Syllabus.objects.all()
    serializer_class =Syllabus_Serializer

class Update_Syllabus_View(generics.UpdateAPIView):
    queryset = Syllabus.objects.all()    
    serializer_class = Syllabus_Serializer

class Delete_Syllabus_View(generics.DestroyAPIView):
    queryset = Syllabus.objects.all()
    serializer_class = Syllabus_Serializer


## for Uploader 

# class Uploader(ModelViewSet):
#     queryset = Uploader.objects.all()
#     serializer_class = Uploader_serializer

#     def get_queryset(self,request,db_field):
#         if db_field.name == 'Subject':
#             category_id = request.POSt.get('category')
#             return 
#         return super().get_queryset()

    # queryset = Uploader.objects.all()
    # serializer_class = Uploader_serializer

class Uploader_ListFiles(generics.ListAPIView):
    queryset = Uploader.objects.all()
    serializer_class = Uploader_serializer

class Uploader_CreateFiles(generics.CreateAPIView):
    queryset = Uploader.objects.all()
    serializer_class = Uploader_serializer        

class Uploader_UpdateFiles(generics.UpdateAPIView):
    queryset = Uploader.objects.all()
    serializer_class = Uploader_serializer            

class Uploader_DeleteFiles(generics.DestroyAPIView):
    queryset = Uploader.objects.all()
    serializer_class = Uploader_serializer        