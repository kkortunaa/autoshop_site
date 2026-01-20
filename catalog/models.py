from django.db import models

# Create your models here.
class CarBrands(models.Model):
    brand = models.CharField("Марка", max_length=128)

    class Meta:
        verbose_name = 'Марка машины'
        verbose_name_plural = 'Марки машины'

    def __str__(self):
        return self.title 

class CarModels(models.Model):
    series = models.SlugField("Серия")
    release_year = models.IntegerField("Год выпуска", max_length=4)
    car_brand = models.ForeignKey(
        CarBrands,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Модель машины'
        verbose_name_plural = 'Модели машины'
    
    def __str__(self):
        return self.title 

class ProductCategory(models.Model):
    category = models.CharField("Категория", max_length=128)

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товара'

    def __str__(self):
        return self.title 
    
# class OrderStatus(models.Model):
#     status_id = models.IntegerField(unique=True)
#     status_name = models.CharField("Статус", max_length=128)
    
#     class Meta:
#         verbose_name = 'Статус'
#         verbose_name_plural = 'Статусы'

#     def __str__(self):
#         return self.title 


class Product(models.Model):
    product_name = models.CharField("Название", max_length=128)
    product_model = models.SlugField()
    product_brand = models.CharField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    product_category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE
    )
    product_car_model = models.ForeignKey(
        CarModels,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары' 
    
    def __str__(self):
        return self.title 

class ProductImages(models.Model):
    image_path = models.CharField()
    image = models.ImageField("Фото", upload_to="products/")
    prod_attr = models.ForeignKey(
        Product,
        related_name="images",
        is_main = models.BooleanField(False),
        on_delete=models.CASCADE
        
    )