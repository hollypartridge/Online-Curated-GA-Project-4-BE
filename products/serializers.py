from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Product, Wardrobe, Wishlist, ShoppingBag
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

class WardrobeSerializer(serializers.ModelSerializer):
    '''Serializer for Wardrobe'''

    class Meta:
        model = Wardrobe
        fields = '__all__'

class NestedWardrobeSerializer(serializers.ModelSerializer):
    '''Serializer for nested wardrobe'''
    owner = NestedUserSerializer()

    class Meta:
        model = Wardrobe
        fields = '__all__'

class ShoppingBagSerializer(serializers.ModelSerializer):
    '''Serializer for Shopping Bag'''

    class Meta:
        model = ShoppingBag
        fields = '__all__'

class NestedShoppingBagSerializer(serializers.ModelSerializer):
    '''Serializer for nested shopping bag'''
    owner = NestedUserSerializer()

    class Meta:
        model = ShoppingBag
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    '''Serializer for outgoing product response'''
    wishlisted_by = NestedWishlistSerializer(many=True, read_only=True)
    in_wardrobe_of = NestedWardrobeSerializer(many=True, read_only=True)
    in_shopping_bag_of = NestedShoppingBagSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'