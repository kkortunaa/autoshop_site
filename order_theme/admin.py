from django.contrib import admin

# Register your models here.
from .models import UserOrder, Bucket, BucketItem

admin.site.register(UserOrder) 
admin.site.register(Bucket) 
