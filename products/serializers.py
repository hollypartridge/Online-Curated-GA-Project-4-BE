from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Product, Wishlist
User = get_user_model()

class NestedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')

class WishlistSerializer(serializers.ModelSerializer):
    '''Serializer for Wishlist'''

    class Meta:
        model = Wishlist
        fields = '__all__'

class NestedWishlistSerializer(serializers.ModelSerializer):
    '''Serializer for nested wishlist'''
    owner = NestedUserSerializer()

    class Meta:
        model = Wishlist
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    '''Serializer for outgoing product response'''
    wishlisted_by = NestedWishlistSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'