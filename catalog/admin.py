from django.contrib import admin
from .models import CarModels, CarBrands, ProductCategory, Product, ProductImages

admin.site.register(CarBrands) 
admin.site.register(CarModels) 
admin.site.register(ProductImages) 
admin.site.register(Product) 
admin.site.register(ProductCategory) 
