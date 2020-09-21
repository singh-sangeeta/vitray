from django.db import models
import users
from products.models import products
from django.db import transaction
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime, timedelta

class cart(models.model):
    user_name = models.ForeignKey(users, null=True,blank=True)
    product_name = models.ManyToManyField(products,blank=True)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    date_created = models.DateField()
    date_deleted = models.DateField()
    date_updated = models.DateField()

class Order(models.Model):
    email = models.EmailField()

class Product(models.Model):
    # ...
    pass

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class coupens(models.Model):
    code = models.CharField(max_length=10, unique=True, blank=True)
    valid_from = models.DateTimeField(default=datetime.now(), blank=True)
    valid_to = models.DateTimeField(default=compute_default_to)
    discount = models.IntegerField(default=15, validators=[MinValueValidator(0), MaxValueValidator(100)])

    active = models.BooleanField(default=True)

class Address(models.Model):
    street = models.TextField()
    city = models.TextField()
    province = models.TextField()
    code = models.TextField()
