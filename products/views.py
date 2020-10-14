from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from products.models import ProductImage, Product, Category, Price
from products.serializers import PriceSerializer, CategorySerializer, ProductSerializer, ProductImageSerializer
from rest_framework import mixins


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ["get","post","put","delete"]
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print(request.data)

        return Response("create response")

    def list(self, request, *args, **kwargs):
        return Response("list response")

    def retrieve(self, request, *args, **kwargs):
        return Response("retrieve response")

    def destroy(self, request, *args, **kwargs):
        return Response("destroy response")

    def update(self, request, *args, **kwargs):
        return Response("update response")


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Category to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductImageViewSet(viewsets.ModelViewSet):
    """
    API endpoints that allows Productimage to be Viewed or edited.
    """
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [permissions.IsAuthenticated]


class PriceViewSets(viewsets.ModelViewSet):
    """
    API endpoints that allows Price to be viewed or edited'
    """
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    permission_classes = [permissions.IsAuthenticated]
