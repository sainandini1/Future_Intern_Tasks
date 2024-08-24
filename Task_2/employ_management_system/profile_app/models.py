
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    desc = models.CharField(null=True,max_length=100 ,blank=True)
    image = models.ImageField(upload_to="images/",null=True ,blank=True)
    name = models.CharField(null=True,max_length=20 ,blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = PhoneNumberField(null=True ,blank=True)
    birth = models.DateField(null=True ,blank=True)

    def __str__(self):
        return self.user.username

   
    
                                
