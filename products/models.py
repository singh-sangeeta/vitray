from django.db import models
from django.contrib.auth.models import User
class products(models.Model):
    product_id = models.AutoField()
    product_name = models.CharField(max_length=50)
    product_details = models.CharField(max_length=100)
    createddate = models.DateField()
    deleteddate = models.DateField()
    updatedate = models.DateField()
    categaries = models.ForeignKey()

class categaries(models.Model):
    id = models.AutoField(primary_Key=True)
    category = models.CharField(max_length=50)

class productimage(models.Model):
    product_id = models.AutoField()
    productimage_id = models.AutoField()
    productimage = models.ImageField()

class price(models.Model):
     product_id = models.AutoField()
     product_price = models.AutoField()
# comment
# comment
# comment
# comment