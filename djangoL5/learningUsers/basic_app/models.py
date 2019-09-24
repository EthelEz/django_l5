from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE,)      #this model class would add in addtional info that the default user doesnt have.

    # Additional Classes
    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):          #NB:This is a method, not an attribute that is going to print the model to the Db
        return self.user.username           #Here username is the default attribute of User
