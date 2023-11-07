from django.db import models

# Create your models here.


class sign_up_datas(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.CharField(max_length=40,unique=True)
    username=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30)