from django.db import models

# Create your models here.

Area_Choice=(    ('top','Top'),
                 ('button','Button'),
                 ('left','left'),
                 ('right','Rignt'))
class Advertisment(models.Model):
    company_name = models.CharField(max_length=255)
    area = models.CharField(max_length=255,choices=Area_Choice,default=1)
    price = models.IntegerField(null=True,blank=True)
    time_added = models.DateTimeField(auto_now_add=True)
