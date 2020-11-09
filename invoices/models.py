from django.db import models

# Create your models here.
class Invoice(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    total = models.CharField(max_length=100)
    paid = models.CharField(max_length=100)
