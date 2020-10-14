
from rest_framework import viewsets
from rest_framework import permissions
from order.models import Cart, Order, OrderProduct, Coupens, Address
from order.serializer import CartSerializer, OrderSerializer, OrderProductSerializer, CoupensSerializer,AddressSerializer


class CartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Cart to be viewed or edited.
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Order to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderProductViewSet(viewsets.ModelViewSet):
    """
    API endpoints that allows OrderProducts to be Viewed or edited.
    """
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class CoupensViewSets(viewsets.ModelViewSet):
    """
    API endpoints that allows Coupens to be viewed or edited'
    """
    queryset = Coupens.objects.all()
    serializer_class = CoupensSerializer
    permission_classes = [permissions.IsAuthenticated]


class AddressViewSets(viewsets.ModelViewSet):
    """
    API endpoints that allows Address to be viewed or edited'
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]
