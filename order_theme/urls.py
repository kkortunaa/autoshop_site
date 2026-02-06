from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="cart"),
    path("cart/", views.cart_view, name="cart"),
    path("checkout/", views.checkout_view, name="checkout"),
    path("add/<int:product_id>", views.add_to_cart, name="add_to_cart"),
    path("increase/<int:item_id>", views.increase_quantity, name="increase_item"),
    path("decrease/<int:item_id>", views.decrease_quantity, name="decrease_item"),
    path("remove/<int:item_id>", views.remove_item, name="remove_item"),
]
