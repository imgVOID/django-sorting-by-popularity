from django.db import models

class ProductType(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=50)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    popularity = models.IntegerField(default=0)
    def __str__(self):
        return self.title