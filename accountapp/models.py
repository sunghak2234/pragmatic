from django.db import models

class helloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)

class HelloWorld2(models.Model):
    text = models.CharField(max_length=100, null=False)