from django.contrib import admin

# Register your models here.
from .models import User_order, ProductInOrder

admin.site.register(User_order) 
admin.site.register(ProductInOrder) 