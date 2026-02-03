from django.db import models

# Create your models here.
class CarBrands(models.Model):
    brand = models.CharField("Марка", max_length=128)

    class Meta:
        verbose_name = 'Марка машины'
        verbose_name_plural = 'Марки машины'
    
    def __str__(self):
        return self.brand


class CarModels(models.Model):
    series = models.SlugField("Серия")
    car_brand = models.ForeignKey(
        CarBrands,
        on_delete=models.CASCADE,
        related_name="model"
    )

    class Meta:
        verbose_name = 'Модель машины'
        verbose_name_plural = 'Модели машины'

    def __str__(self):
        return self.series
    

class ProductCategory(models.Model):
    category = models.CharField("Категория", max_length=128)

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товара'

    def __str__(self):
        return self.category


class Product(models.Model):
    product_name = models.CharField("Название", max_length=128)
    product_model = models.SlugField()
    product_brand = models.CharField()
    price = models.DecimalField(decimal_places=2, max_digits=9)
    product_category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        related_name="product_category"
    )
    car_models = models.ManyToManyField(
        CarModels,
        blank=True,
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары' 
    
    def __str__(self):
        return self.product_name

class ProductImages(models.Model):
    image = models.ImageField("Фото", upload_to="products/")
    is_main = models.BooleanField(default=False)
    prod_attr = models.ForeignKey(
        Product,
        related_name="images",
        on_delete=models.CASCADE
        
    )
    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото' 

    def __str__(self):
        return self.image.name
    
    @property
    def main_image(self):
        return self.images.filter(is_main=True).first() or self.images.first()