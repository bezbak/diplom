from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    full_name = models.CharField(
        'ФИО пользователя',
        max_length=255,
        blank=True, null=True
    )
    phone_number = models.CharField(
        'Номер телефона',
        max_length=20,
        blank=True, 
        null=True
    )
    profile_image = models.ImageField(
        'Фото профиля',
        upload_to='profiles/'
    )
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        
class Category(models.Model):
    name = models.CharField(
        'Название категории',
        max_length=100
    )
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
class Product(models.Model):
    title = models.CharField(
        'Название продукта',
        max_length=255
    )
    price = models.IntegerField(
        'Цена продукта'
    )
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
    )
    description = models.TextField(
        'Описание продукта'
    )
    image = models.ImageField(
        'Фото продукта',
        upload_to='products/'
    )
    
    def __str__(self):
        return f"{self.title} - {self.category.name}"
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        
class Cart(models.Model):
    user = models.ForeignKey(
        User,
        related_name='cart',
        on_delete=models.CASCADE
    )
    date = models.DateField(
        auto_now_add=True
    )
    amount = models.IntegerField(
        'Сумма'
    )
    
    def __str__(self):
        return f"Корзинка пользователя {self.user.username}"
    
    class Meta:
        verbose_name = 'Корзинка'
        verbose_name_plural = 'Корзинки'
        
class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, 
        related_name='items',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, 
        related_name='items',
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(
        'Количество'
    )
    
    def __str__(self):
        return f"{self.product.title} - {self.quantity}"
    
    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'