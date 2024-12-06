from django.db import models

# Create your models here.

class Emp(models.Model):
    empname=models.CharField(max_length=100)
    empid=models.IntegerField(primary_key=True)
    email=models.EmailField()