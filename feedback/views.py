
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from feedback.models import ReviewProduct
from feedback.serializer import ReviewProductSerializer


class ReviewProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ReviewProduct to be viewed or edited.
    """

    queryset = ReviewProduct.objects.all()
    serializer_class = ReviewProductSerializer
    permission_classes = [permissions.IsAuthenticated]

