from django.contrib import admin
from . import models

admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(models.Product_image)
admin.site.register(models.Price)
