from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200, null=True)
    file = models.FileField(upload_to='product/', null=True, blank=True)