from django.db import models


class Product(models.Model):
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    name_product = models.CharField(max_length=30)
    size = models.CharField(max_length=1, choices=SIZES)
    color = models.CharField(max_length=100)
    amount =  models.CharField(max_length=999)


