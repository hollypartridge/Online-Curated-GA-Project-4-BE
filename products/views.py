from rest_framework.generics import (
    ListAPIView, 
    RetrieveUpdateAPIView, 
    CreateAPIView, 
    DestroyAPIView
)
from rest_framework.permissions import IsAuthenticated

from .permissions import isOwnerOrReadyOnly
from .models import Product, Wishlist, Wardrobe, ShoppingBag
from .serializers import (
    ProductSerializer, 
    WishlistSerializer, 
    WardrobeSerializer, 
    ShoppingBag, 
    ShoppingBagSerializer
)

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class WishlistListView(CreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = (IsAuthenticated, )

class WishlistDetailView(DestroyAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = (IsAuthenticated, )

class WardrobeListView(CreateAPIView):
    queryset = Wardrobe.objects.all()
    serializer_class = WardrobeSerializer
    permission_classes = (IsAuthenticated, )

class WardrobeDetailView(DestroyAPIView):
    queryset = Wardrobe.objects.all()
    serializer_class = WardrobeSerializer
    permission_classes = (IsAuthenticated, )

class ShoppingBagListView(CreateAPIView):
    queryset = ShoppingBag.objects.all()
    serializer_class = ShoppingBagSerializer
    permission_classes = (IsAuthenticated, )

class ShoppingBagDetailView(DestroyAPIView):
    queryset = ShoppingBag.objects.all()
    serializer_class = ShoppingBagSerializer
    permission_classes = (IsAuthenticated, )