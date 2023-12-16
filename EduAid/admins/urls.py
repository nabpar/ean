from django.urls import path,include
from rest_framework.routers import DefaultRouter
# from .views import Create_Category_View,List_Category_view,Update_Category_View,Delete_Category_View,List_Syllabus_view
from . import views





# router = DefaultRouter()
# router.register(r'uploader/',views.Uploader,basename="uploader")

urlpatterns = [
    # For search
    path('search_categorys/',views.SearchCategory.as_view(),name = "CategorySearch"),

    
    # For Category
    path('create_categorys/',views.Create_Category_View.as_view(),name="reate_Category"),
    path('view_categorys/',views.List_Category_view.as_view(),name="category_view"),
    path('update_categorys/<int:pk>/',views.Update_Category_View.as_view(),name="Update_Category"),
    path('delete_categorys/<int:pk>/',views.Delete_Category_View.as_view(),name="Delete_Category"),

    # For Subject
    path('category_subjects',views.Create_Subject_View.as_view(),name="Create_Subject"),
    path('view_subject/s',views.List_Subject_view.as_view(),name="liist_cSubject"),
    path('update_subjects/<int:pk>/',views.Update_Subject_View.as_view(),name="Update_Subject"),
    path('delete_subjects/<int:pk>/',views.Delete_Subject_View.as_view(),name="Delete_Subject"),

    # For Topic
    path('create_topics/',views.Create_Topic_View.as_view(),name="Create_Topic"),
    path('view_topic/s',views.List_Topic_view.as_view(),name="topic_view"),
    path('update_topics/<int:pk>/',views.Update_Topic_View.as_view(),name="Update_Topic"),
    path('delete_topics/<int:pk>/',views.Delete_Topic_View.as_view(),name="Delete_Topic"),


     # For Subtopic
    path('create_subtopics/',views.Create_Subtopic_View.as_view(),name="Create_Subtopic"),
    path('view_subtopics/',views.List_Subtopic_view.as_view(),name="Subtopic_View"),
    path('update_subtopics/<int:pk>/',views.Update_Subtopic_View.as_view(),name="Update_Subtopic"),
    path('delete_subtopics/<int:pk>/',views.Delete_Subtopic_View.as_view(),name="Delete_Subtopic"),


 # For Syllabus
    path('create_syllabus/',views.Create_Syllabus_View.as_view(),name="Create_Syllabus"),
    path('view_syllabus/',views.List_Syllabus_view.as_view(),name="Syllabus_View"),
    path('update_syllabus/<int:pk>/',views.Update_Syllabus_View.as_view(),name="Update_Syllabus"),
    path('delete_syllabus/<int:pk>/',views.Delete_Syllabus_View.as_view(),name="Delete_Syllabus"),


   ## for uploader
#    path('uploader/',include(router.urls)), 
path('view_files/',views.Uploader_ListFiles.as_view(),name="view files"),
path('create_files/',views.Uploader_CreateFiles.as_view(),name="create files"),
path('update_files/',views.Uploader_UpdateFiles.as_view(),name="updare files"),
path('delete_files/',views.Uploader_DeleteFiles.as_view(),name="delete files"),
]
