from rest_framework import serializers
from order.models import Cart, Order, OrderProduct, Coupens, Address


class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ['user_name', 'total_price', 'product_name', 'date_created', 'date_deleted', 'date_updated']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['user', 'product_name', 'email', 'status']


class OrderProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['order', 'quantity']


class CoupensSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coupens
        fields = ['code', 'valid_from', 'valid_to', 'discount', 'active']


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ['street', 'city', 'province', 'code']
