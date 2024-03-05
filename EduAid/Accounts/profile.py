
from django.db import models
from .models import User


class Profile(models.Model):
    user_email = models.OneToOneField(User,on_delete=models.CASCADE,related_name = 'profile')
    name= models.CharField(max_length = 255,blank=True,null=True)
    contact = models.BigIntegerField(blank=True,null=True)
    image = models.ImageField(upload_to='media',blank=True,null=True)
    # status = models.CharField(max_length = 255,blank=True,null = True)


    def save(self,*args,**kwargs):
        if self.user_email:
            self.name = self.user_email.name
            self.contact = self.user_email.contact

        return super().save(args,kwargs)
    

    def __str__(self):
        return self.name
    

    class Meta:
        db_table = 'profiles'
     