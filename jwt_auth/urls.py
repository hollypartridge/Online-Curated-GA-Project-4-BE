from django.urls import path
from .views import UserProfileView, UserRegisterView, UserLoginView

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('profile/<int:pk>/', UserProfileView.as_view()),
]