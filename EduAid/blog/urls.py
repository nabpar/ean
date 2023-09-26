from django.urls import path

from blog import views

urlpatterns = [
    # this is the Blog Url
    path("viewlist/", views.View_Blog.as_view(), name="view"),
    path("create/", views.Create_Blog.as_view(), name="view"),
    path("view_resource/", views.Create_Resource.as_view()),
    path("update_resource/", views.Update_Resource.as_view()),
    path("destroy_resource/", views.Delete_Resource.as_view()),
]
