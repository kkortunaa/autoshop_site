from django.db import models
from catalog.models import Product


class User_order(models.Model):

    class ModelChoices(models.TextChoices):
        IN_PROGRESS = "в процессе",
        IN_WAY = "в пути",
        READY = "Готов",
        ERROR = "Ошибка",

    name = models.CharField("Имя", max_length=128)
    phone_number = models.CharField("Номер телефона", max_length=20)
    status = models.CharField("Статус", max_length=128, choices=ModelChoices.choices, default=ModelChoices.IN_PROGRESS)
    session_key = models.CharField(unique=True, max_length=40)
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
    
    def __str__(self):
        return self.name 

class Bucket(models.Model):
    session_key = models.CharField(unique=True, max_length=40)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return self.session_key


class BucketItem(models.Model):
    price_in_moment = models.IntegerField()
    quantity = models.IntegerField(default=1)
    bucket = models.ForeignKey(
        Bucket,
        related_name="products",
        on_delete=models.CASCADE
    )
    prod = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    class Meta:
        verbose_name = 'Товар корзины'
        verbose_name_plural = 'Товары корзины'
