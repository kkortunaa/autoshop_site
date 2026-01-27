from django.shortcuts import render
from catalog.models import Product

def catalog_view(request):
    products = Product.objects.all().prefetch_related(
        'images',
        'car_models__car_brand',
        'product_category'
    )
    return render(request, 'catalog.html', {'products': products})

def product_detail_view(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})