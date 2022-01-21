from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    '''Serializer for outgoing product response'''

    class Meta:
        model = Product
        fields = '__all__'