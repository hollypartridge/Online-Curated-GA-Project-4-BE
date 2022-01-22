from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .permissions import isOwnerOrReadyOnly

from .models import Product, Wishlist
from .serializers import ProductSerializer, WishlistSerializer

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
    permission_classes = (isOwnerOrReadyOnly, )