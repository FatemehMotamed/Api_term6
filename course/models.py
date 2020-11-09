from django.db import models

# Create your models here.



class Course(models.Model):
    name = models.CharField(max_length=25)
    type = models.CharField(max_length=25)
    price = models.CharField(max_length=15)
    author = models.CharField(max_length=25)
    page_number = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
