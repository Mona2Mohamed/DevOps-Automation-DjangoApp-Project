from django.db import models

# Create your models here.
class Patient(models.Model):
    id =  models.IntegerField(primary_key=True)
    Username =models.CharField(max_length=50,blank=True)
    Password= models.CharField(max_length=100,blank=True) 
    Re_type = models.CharField(max_length=100,blank=True)
    First_name = models.CharField(max_length=50,blank=True)
    Last_name = models.CharField(max_length=50,blank=True)
    DateOfBirth = models.DateField(default='2023-11-10')



