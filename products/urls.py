from django.urls import path
from .views import ProductListView, ProductDetailView, WishlistListView, WishlistDetailView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('<int:pk>/', ProductDetailView.as_view()),
    path('<int:pk>/wishlist/', WishlistListView.as_view()),
    path('<int:products_pk>/wishlist/<int:pk>/', WishlistDetailView.as_view()),
]