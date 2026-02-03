from django.shortcuts import render, redirect, get_object_or_404
from .models import Bucket, BucketItem
from catalog.models import Product

def index():
    pass

def _get_session_key(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key


def add_to_cart(request, product_id):
    if request.method != "POST":
        return redirect("cart")
    session_key = _get_session_key(request)
    bucket, _ = Bucket.objects.get_or_create(session_key=session_key)
    product = get_object_or_404(Product, pk=product_id)
    item, created = BucketItem.objects.get_or_create(
        bucket=bucket,
        prod=product,
        defaults={"price_in_moment": product.price, "quantity": 1},
    )   

    if not created:
        item.quantity += 1
        item.save()

# После добавления товара перенаправляем пользователя на страницу корзины
    return redirect("cart")

def cart_view(request):
    session_key = _get_session_key(request)
    bucket, _ = Bucket.objects.get_or_create(session_key=session_key)
    prods = list(bucket.products.select_related("prod"))
    prods = [prod.prod for prod in prods]
    return render(request, 'cart.html', {"prods":prods})

def increase_quantity(request, item_id):
    delta = 1
    return _change_quantity(request,item_id, delta)


def decrease_quantity(request, item_id):
    delta = -1
    return _change_quantity(request,item_id, delta)

def _change_quantity(request, item_id, delta):
    if request.method != "POST":
        return redirect("cart")
    session_key = _get_session_key(request)
    bucket, _ = Bucket.objects.get_or_create(session_key=session_key)
    item = get_object_or_404(BucketItem, prod_id = item_id, bucket=bucket)
    new_quantity = item.quantity + delta
    if new_quantity <= 0:
        item.delete()
    else:
        item.quantity = new_quantity
        item.save(update_fields=["quantity"])
    
    return redirect("cart")