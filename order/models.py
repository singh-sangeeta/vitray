import product
from django.db import models
import users
from products.models import products

class cart(models.model):
    user_name = models.ForeignKey(users, null=True,blank=True)
    product_name = models.ManyToManyField(products,blank=True)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    date_created = models.DateField()
    date_deleted = models.DateField()
    date_updated = models.DateField()

class Item(models.Model):
    item = models.ForeignKey(product, null=True)
    cart = models.ForeignKey(cart, null=True)
    quantity = models.PositiveIntegerField()
