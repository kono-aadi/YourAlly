from django.db import models

# Create your models here.
class Task_add(models.Model):
    Task_heading=models.CharField(max_length=50,default="",null=True)
    Task_description=models.CharField(max_length=300,default='',null=True)
    Email=models.CharField(max_length=50,default='',null=True)
    Id=models.CharField(max_length=5,default='',null=True)
