from django.urls import path
from .views import ( 
    ProductListView, 
    ProductDetailView, 
    WishlistListView, 
    WishlistDetailView, 
    WardrobeListView, 
    WardrobeDetailView,
    ShoppingBagListView,
    ShoppingBagDetailView
)

urlpatterns = [
    path('', ProductListView.as_view()),
    path('<int:pk>/', ProductDetailView.as_view()),
    path('<int:pk>/wishlist/', WishlistListView.as_view()),
    path('<int:products_pk>/wishlist/<int:pk>/', WishlistDetailView.as_view()),
    path('<int:pk>/wardrobe/', WardrobeListView.as_view()),
    path('<int:products_pk>/wardrobe/<int:pk>/', WardrobeDetailView.as_view()),
    path('<int:pk>/shoppingbag/', ShoppingBagListView.as_view()),
    path('<int:products_pk>/shoppingbag/<int:pk>/', ShoppingBagDetailView.as_view()),
]