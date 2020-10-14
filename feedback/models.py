from django.db import models

from products.models import Product


class ReviewProduct(models.Model):
    product = models.ForeignKey( Product, on_delete = models.CASCADE, default = 1 )
    rating = models.IntegerField()
    comment = models.TextField()
