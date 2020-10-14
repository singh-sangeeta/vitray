from django.db import models
from django.utils.timezone import now


class Category( models.Model ):
    category = models.CharField( max_length = 50 )
    date_created = models.DateField(null = True)
    date_deleted = models.DateField(null = True)
    date_updated = models.DateField(null = True)


class Product( models.Model ):
    product_name = models.CharField( max_length = 50 )
    product_details = models.CharField( max_length = 100 )
    category = models.ForeignKey( Category, on_delete = models.DO_NOTHING,default = 1)
    date_created = models.DateField(null = True)
    date_deleted = models.DateField(null = True)
    date_updated = models.DateField(null = True)


class ProductImage( models.Model ):
    product = models.ForeignKey( Product, on_delete = models.CASCADE,default = 1 )
    product_image = models.ImageField( blank = True, null = True )
    date_created = models.DateField( default = now )
    date_deleted = models.DateField(null = True)
    date_updated = models.DateField(null = True)


class Price( models.Model ):
    product = models.ForeignKey( Product, on_delete = models.CASCADE,default = 1)
    product_price = models.IntegerField()

