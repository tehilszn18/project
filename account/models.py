from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, null=True)    
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(default='', null=True)
    phone_number = models.IntegerField(null=True)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=20, choices=(('MALE', 'Male'),('FEMALE', 'Female')
    , ('UNSPECIFIED', 'Unspecified')), null=True)
    residential_address = models.CharField(max_length=100, null=True)
    state_of_residence = models.CharField(max_length=100, null=True)
    

    def __str__(self) -> str:
        return f'{self.user}'
