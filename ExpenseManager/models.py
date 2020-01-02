from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


# class UserProfileInfo(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     portfolio_site = models.URLField(blank=True)
#     bio = models.CharField(blank=True,max_length=50)
#
#     def __str__(self):
#       return self.user.username




class Category(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=1,primary_key=True)
    name = models.CharField(blank=True, max_length=20,null=True,default='Cake')
    total_expense = models.IntegerField(blank=True,null=True,default=0)
    datefield = models.DateField(blank=True,default='2012-12-12',null=True)
    petrol_datefield = models.DateField(blank=True,default='2012-12-12',null=True)
    clothes_datefield = models.DateField(blank=True,default='2012-12-12',null=True)
    petrol_total_expense = models.IntegerField(blank=True,default=0,null=True)
    clothes_total_expense = models.IntegerField(blank=True,default=0,null=True)
    cloth_type = models.CharField(blank=True, max_length=20,null=True, default='Jeans')

    def __str__(self):
        return self.user.username

class Date(models.Model):
    #userName = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    dateField = models.DateField(blank=True,default='2019-01-01')
    foodname = models.CharField(blank=True,max_length=20,null=True)
    food_expense = models.IntegerField(blank=True,null=True,default=1)
    petrol_expense = models.IntegerField(blank=True,null=True,default=1)
    cloth_expense = models.IntegerField(blank=True,null=True,default=1)
    total_expense = models.IntegerField(blank=True,null=True,default=1)

    def __str__(self):
        return str(self.dateField)
