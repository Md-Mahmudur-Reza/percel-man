from django.db import models


class Destination(models.Model):
    destination = models.CharField(max_length=100)
    def __str__(self):
        return self.destination

class Merchant(models.Model):
    merchant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    products = models.TextField()
    total_weight = models.IntegerField()
    destinations = models.ForeignKey(Destination, on_delete=models.CASCADE)
    def __str__(self):
        a= self.merchant_id
        a = str(a)
        return a


class Product(models.Model):
    percel_id = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=100) 
    def __str__(self):
        return self.product_type


