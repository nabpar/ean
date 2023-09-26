from django.contrib import admin

from .models import Blog, ResourceUploader

# Register your models here.


class Blog_Admin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "category",
        "content",
        "image",
        "date_created",
        "date_updated",
        "created_by",
        "slug",
    )


admin.site.register(Blog, Blog_Admin)


class Resource_Admin(admin.ModelAdmin):
    list_display = (
        "blog",
        "comment",
        "date",
    )


admin.site.register(ResourceUploader, Resource_Admin)
