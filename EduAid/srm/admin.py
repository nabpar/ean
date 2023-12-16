from django.contrib import admin

# Register your models here.


from .models import Advertisment

class Admin_Advertisment(admin.ModelAdmin):
    list_display=['company_name','area','price','time_added']
admin.site.register(Advertisment,Admin_Advertisment)    