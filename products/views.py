from rest_framework import generics, viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from .models import User, Product, Cart, Category, CartItem
from .serializers import RegisterSerializer, UserSerializer, ProductSerializer, CategorySerializer, CartItemSerializer, CartSerializer, CartItemCreateSerializer
from rest_framework.response import Response
class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer    
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ['title', 'description']
    filterset_fields = ('category',)
    
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('user',)
    
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    
    def get_serializer_class(self):
        if self.action == "create":
            return CartItemCreateSerializer
        return CartItemSerializer
    
    def create(self, request, *args, **kwargs):
        cart_id = request.data.get('cart')
        product_id = request.data.get('product')
        quantity = request.data.get('quantity', 1)

        if not all([cart_id, product_id]):
            return Response({"detail": "Missing cart or product"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Используем filter вместо get_or_create для поиска существующих записей
            cart_items = CartItem.objects.filter(cart_id=cart_id, product_id=product_id)
            if cart_items.exists():
                # Если товары найдены, обновляем количество первой записи
                cart_item = cart_items.first()
                cart_item.quantity += int(quantity)
                cart_item.save()
                created = False
            else:
                # Если товар не найден, создаем новый
                cart_item = CartItem.objects.create(cart_id=cart_id, product_id=product_id, quantity=quantity)
                created = True

            serializer = self.get_serializer(cart_item)
            return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)