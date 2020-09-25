from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from datetime import datetime

from django.core.validators import MinValueValidator, MaxValueValidator


class cart(models.Model):
    user_name = models.ForeignKey(User, null=False, blank=False, on_delete=models.SET(User))
    price_total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    product_name = models.ForeignKey(Product, null=False, blank=False, on_delete=models.SET(Product))
    date_created = models.DateField()
    date_deleted = models.DateField()
    date_updated = models.DateField()


class Order(models.Model):
    user = models.ForeignKey(User, null=False, blank=False,  on_delete=models.SET(User))
    product_name = models.ForeignKey(Product, null=False, blank=False, on_delete=models.SET(Product))
    status = models.CharField(max_length=20)
    email = models.EmailField()


class Order_Product(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class Coupens(models.Model):
    code = models.CharField(max_length=10, unique=True, blank=True)
    valid_from = models.DateTimeField(default=datetime.now(), blank=True, null=True)
    valid_to = models.DateTimeField(default=compute_default_to)
    discount = models.IntegerField(default=15, validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField(default=True)


class Address(models.Model):
    street = models.TextField()
    city = models.TextField()
    province = models.TextField()
    code = models.TextField()
