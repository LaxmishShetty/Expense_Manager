from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    bio = models.CharField(blank=True,max_length=50)

    def __str__(self):
      return self.user.username