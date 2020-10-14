from rest_framework import serializers
from feedback.models import ReviewProduct


class ReviewProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReviewProduct
        fields = ['product', 'rating', 'comment']