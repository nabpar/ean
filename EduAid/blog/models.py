from django.db import models

from admins.models import Category
from django.utils.text import slugify

# Create your models here.


def File(instance, filename):
    return "image/{filename}".format(filename=filename)


class Blog(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="data_from_category"
    )
    content = models.CharField(max_length=100)
    image = models.ImageField(upload_to=File, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, null=True, blank=True)




    def save(self,*args,**krgs):
        if not self.slug:
            self.slug = slugify(self.title)
        self.slug = slugify(self.slug)
        super(Blog,self).save(*args,**krgs)    

    def __str__(self):
        return self.title


class ResourceUploader(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name="Resourceuploader_from_blog",
        null=True,
    )
    comment = models.TextField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
