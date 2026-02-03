from django.contrib import admin
from .models import CarModels, CarBrands, ProductCategory, Product, ProductImages

class ProductImagesInLine(admin.TabularInline):
    model = ProductImages
    fields = ("image", "is_main")
    
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductImagesInLine,)

admin.site.register(CarBrands) 
admin.site.register(CarModels) 
admin.site.register(ProductImages) 
admin.site.register(Product, ProductAdmin) 
admin.site.register(ProductCategory) 
