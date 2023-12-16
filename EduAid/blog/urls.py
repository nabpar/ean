from django.urls import path

from blog import views


urlpatterns = [
    # this is the Blog Url
    path("view_blogs/", views.View_Blog.as_view(), name="ViewBlogs"),
    path("create_blogs/", views.Create_Blog.as_view(), name="CreateBlogs"),
    path("view_resources", views.Create_Resource.as_view()),
    path("update_resources/", views.Update_Resource.as_view()),
    path("delete_resources/", views.Delete_Resource.as_view()),


    path("search_blogs/",views.SearchList.as_view(),name="SearchBlogs"),
    # path('mmvs/',views.MyModelViewSet.as_view(),name="viewset"),
]
