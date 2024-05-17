from django.urls import path, include
from rest_framework import routers 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'cart/items', CartItemViewSet)
router.register(r'users', UserViewSet)
router.register(r'cart', CartViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
