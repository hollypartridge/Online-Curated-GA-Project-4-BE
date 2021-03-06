from rest_framework import serializers
from django.contrib.auth import get_user_model
import django.contrib.auth.password_validation as validation
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.conf import settings

from products.models import Product, Wishlist, Wardrobe, ShoppingBag

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, attrs):
        password = attrs.pop('password')
        password_confirmation = attrs.pop('password_confirmation')

        if password != password_confirmation:
            raise ValidationError({'detail':'Password and Confirmation do not match'})

        if settings.ENV != 'DEV':
            try:
                validation.validate_password(password=password)
            except ValidationError as err:
                raise ValidationError({'password': err})

        attrs['password'] = make_password(password)

        return attrs

    class Meta:
        model = User
        fields = '__all__'

class NestedProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'designer', 'description', 'image', 'color', 'price', 'category', 'type')

class NestedWishlistSerializer(serializers.ModelSerializer):
    product = NestedProductSerializer()

    class Meta:
        model = Wishlist
        fields = '__all__'

class NestedWardrobeSerializer(serializers.ModelSerializer):
    product = NestedProductSerializer()

    class Meta:
        model = Wardrobe
        fields = '__all__'

class NestedShoppingBagSerializer(serializers.ModelSerializer):
    product = NestedProductSerializer()

    class Meta:
        model = ShoppingBag
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    wishlisted_products = NestedWishlistSerializer(many=True)
    products_in_wardrobe = NestedWardrobeSerializer(many=True)
    products_in_shopping_bag = NestedShoppingBagSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'wishlisted_products', 'products_in_wardrobe', 'products_in_shopping_bag')