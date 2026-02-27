from django.db import models

# Create your models here.
class Data(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    age=models.CharField(max_length=10)
    salary=models.CharField(max_length=20)