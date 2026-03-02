from django.db import models


# Create your models here.
class Data(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    location=models.CharField(max_length=100,blank=True)
    age=models.IntegerField()
    salary=models.PositiveIntegerField()