from django.shortcuts import render
from catalog.models import Product
from django.core.paginator import Paginator


def catalog_view(request):
    products = Product.objects.all().prefetch_related(
        'images',
        'car_models__car_brand',
        'product_category'
    )
    # paginator = Paginator(products, 15)
    # page_obj = paginator.get_page(request.GET.get("page"))



    return render(request, 'catalog.html', {'products': products}, )

def product_detail_view(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})