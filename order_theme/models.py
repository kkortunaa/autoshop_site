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
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
    
    def __str__(self):
        return self.name 


class ProductInOrder(models.Model):
    price_in_moment = models.IntegerField()
    quantity = models.IntegerField()
    product_attr = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    order_attr = models.ForeignKey(
        User_order,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе' 
    
