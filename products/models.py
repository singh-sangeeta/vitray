from django.db import models
from django.contrib.auth.models import User
class products(models.Model):
    product_id = models.AutoField()
    product_name = models.CharField(max_length=50)
    product_details = models.CharField(max_length=100)
    categaries = models.ForeignKey(categaries,null=True,blank=True)
    date_created = models.DateField()
    date_deleted = models.DateField()
    date_updated = models.DateField()

class categaries(models.Model):
    id = models.AutoField(primary_Key=True)
    category = models.CharField(max_length=50)
    date_created = models.DateField()
    date_deleted = models.DateField()
    date_updated = models.DateField()

class productimage(models.Model):
    product_id = models.AutoField()
    productimage_id = models.AutoField()
    product_image = models.ImageField(blank=True,null=True)
    date_created = models.DateField()
    date_deleted = models.DateField()
    date_updated = models.DateField()

class price(models.Model):
     product_id = models.AutoField()
     product_price = models.AutoField()



# comment
# comment
# comment
# comment