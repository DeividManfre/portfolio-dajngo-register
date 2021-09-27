from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField()
    password = models.CharField(max_length = 150, null=False)

class Product(models.Model):
    sizee = [
        ('P' , 'little'),
        ('M' , 'medium'),
        ('G' , 'great'),
    ]
    name = models.CharField(max_length = 150, null=False)
    code = models.CharField(max_length=150, null=True)
    size = models.CharField(max_length=1, choices=sizee ,null=True)
