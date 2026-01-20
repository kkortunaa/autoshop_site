from django.db import models
from catalog.models import Product

class User_order(models.Model):
    name = models.CharField("Имя", max_length=128)
    phone_number = models.SlugField("Номер")
    status = models.CharField("Статус", max_length=128)
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
    
    def __str__(self):
        return self.title 


class ProductInOrder(models.Model):
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
    
    def __str__(self):
        return self.title 


