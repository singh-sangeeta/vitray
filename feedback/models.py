from django.db import models
from products.models import products
class revieewproduct(models.Model):
    product_id = models.ForeignKey(products,null=True,blank=True)
    rating = models.AutoField()
    comments = models.TextField()

