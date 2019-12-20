from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# class UserProfileInfo(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     portfolio_site = models.URLField(blank=True)
#     bio = models.CharField(blank=True,max_length=50)
#
#     def __str__(self):
#       return self.user.username




class Category(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=1)
    name = models.CharField(blank=True, max_length=20,null=True,default='Cake')
    total_expense = models.IntegerField(blank=True,null=True,default=1)
    datefield = models.DateField(blank=True,null=True,default='2012/12/12')
    petrol_total_expense = models.IntegerField(blank=True,default=1,null=True)
    clothes_total_expense = models.IntegerField(blank=True,default=1,null=True)
    cloth_type = models.CharField(blank=True,max_length=20,null=True,default='Jeans')

    def __str__(self):
        return self.user.username


