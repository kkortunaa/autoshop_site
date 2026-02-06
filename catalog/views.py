from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from catalog.models import Product, ProductCategory
from django.core.paginator import Paginator


def catalog_view(request):
    products = Product.objects.all().prefetch_related(
        'images',
        'car_models__car_brand',
        'product_category'
    )
    categories = ProductCategory.objects.all()
    query = request.GET.get("q")
    category_id = request.GET.get("category")
    brand = request.GET.get("brand")
    price_min = request.GET.get("price_min")
    price_max = request.GET.get("price_max")
    sort = request.GET.get("sort", "popular")

    if query:
        products = products.filter(
            Q(product_name__icontains=query) | Q(product_model__icontains=query)
        )

    if category_id:
        products = products.filter(product_category_id=category_id)

    if brand:
        products = products.filter(product_brand__icontains=brand)

    if price_min:
        products = products.filter(price__gte=price_min)

    if price_max:
        products = products.filter(price__lte=price_max)

    if sort == "price_asc":
        products = products.order_by("price")
    elif sort == "price_desc":
        products = products.order_by("-price")
    elif sort == "new":
        products = products.order_by("-id")
    else:
        products = products.order_by("-id")

    paginator = Paginator(products, 9)
    page_obj = paginator.get_page(request.GET.get("page"))

    context = {
        "page_obj": page_obj,
        "categories": categories,
    }
    return render(request, "pages/catalog.html", context)


def product_detail_view(request, product_id):
    product = get_object_or_404(
        Product.objects.prefetch_related(
            "images",
            "car_models__car_brand",
            "product_category",
        ),
        id=product_id,
    )

    related_products = (
        Product.objects.filter(product_category=product.product_category)
        .exclude(id=product.id)
        .prefetch_related("images")[:4]
    )

    context = {
        "product": product,
        "related_products": related_products,
    }
    return render(request, "pages/product_detail.html", context)
