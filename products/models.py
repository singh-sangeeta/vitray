from django.db import models
from django.contrib.auth.models import User
class products(models.Model):
    productid = models.IntegerField()
    productname = models.CharField(max_length=50)
    productdetails = models.CharField(max_length=100)
    createddate = models.DateField()
    deleteddate = models.DateField()
    updatedate = models.DateField()
# Create your models here.
# comment
# comment
# comment
# comment