from django.shortcuts import render, redirect, get_object_or_404
from .models import Bucket, BucketItem
from catalog.models import Product

def index(request):
    return cart_view(request)

def _get_session_key(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key


def add_to_cart(request, product_id):
    if request.method != "POST":
        return redirect("cart")

    try:
        quantity = int(request.POST.get("quantity", 1))
    except (TypeError, ValueError):
        quantity = 1
    quantity = max(1, quantity)

    session_key = _get_session_key(request)
    bucket, _ = Bucket.objects.get_or_create(session_key=session_key)
    product = get_object_or_404(Product, pk=product_id)
    item, created = BucketItem.objects.get_or_create(
        bucket=bucket,
        prod=product,
        defaults={"price_in_moment": product.price, "quantity": quantity},
    )   

    if not created:
        item.quantity += quantity
        item.save()

    return redirect("cart")

def cart_view(request):
    session_key = _get_session_key(request)
    bucket, _ = Bucket.objects.get_or_create(session_key=session_key)
    cart_items = list(
        bucket.products.select_related("prod").prefetch_related("prod__images")
    )

    total_items = 0
    subtotal = 0
    for item in cart_items:
        item.line_total = item.price_in_moment * item.quantity
        total_items += item.quantity
        subtotal += item.line_total

    context = {
        "cart_items": cart_items,
        "total_items": total_items,
        "subtotal": subtotal,
        "cart_items_count": total_items,
    }
    return render(request, "pages/cart.html", context)

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


def remove_item(request, item_id):
    if request.method != "POST":
        return redirect("cart")
    session_key = _get_session_key(request)
    bucket, _ = Bucket.objects.get_or_create(session_key=session_key)
    item = get_object_or_404(BucketItem, prod_id=item_id, bucket=bucket)
    item.delete()
    return redirect("cart")


def checkout_view(request):
    return render(request, "pages/checkout.html")
