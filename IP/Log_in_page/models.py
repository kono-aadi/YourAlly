from django.db import models

# Create your models here.


class Log_in_datas(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

class Check(models.Model):
    un=models.CharField(max_length=23)
    IN=models.CharField(max_length=23)

