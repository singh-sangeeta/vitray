from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from products.models import Product


class Cart(models.Model):
    user_name = models.ForeignKey(User, null=False, blank=False, on_delete=models.SET(User))
    total_price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    product_name = models.ForeignKey(Product, null=False, blank=False, on_delete=models.SET(Product))
    date_created = models.DateField(null = True)
    date_deleted = models.DateField(null = True)
    date_updated = models.DateField(null = True)


class Order(models.Model):
    user = models.ForeignKey(User, null=False, blank=False,  on_delete=models.SET(User))
    product_name = models.ForeignKey(Product, null=False, blank=False, on_delete=models.SET(Product))
    status = models.CharField(max_length=20)
    email = models.EmailField()


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class Coupens(models.Model):
    code = models.CharField(max_length=10, unique=True, blank=True)
    valid_from = models.DateField(null = True, blank = True)
    valid_to = models.DateField(null = True,)
    discount = models.IntegerField(default=15, validators=[MinValueValidator(0), MaxValueValidator(100)])

    active = models.BooleanField(default=True)


class Address(models.Model):
    street = models.TextField()
    city = models.TextField()
    province = models.TextField()
    code = models.TextField()
