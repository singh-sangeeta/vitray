
from rest_framework import serializers
from products.models import ProductImage, Category, Product, Price


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'product_details', 'category', 'date_created', 'date_deleted', 'date_updated']


class ProductImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['product', 'product_image', 'date_created', 'date_deleted', 'date_updated']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['category', 'date_created', 'date_deleted', 'date_updated']


class PriceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Price
        fields = ['product', 'product_price']