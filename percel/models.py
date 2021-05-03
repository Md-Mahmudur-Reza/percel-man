from django.db import models


class Destination(models.Model):
    destination = models.CharField(max_length=100)
    def __str__(self):
        return self.destination

class Merchant(models.Model):
    name = models.CharField(max_length=100)
    products = models.TextField()
    total_weight = models.IntegerField()
    destinations = models.ForeignKey(Destination,null=False, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


ProductTypeChoice = [
    ('fragile', 'Fragile'),
    ('liquid', 'Liquid'),
    ('solid', 'Solid'),
]
class Product(models.Model):
    percel_id = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=100, choices=ProductTypeChoice) 
    def __str__(self):
        return self.product_type


