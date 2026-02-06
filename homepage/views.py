from django.shortcuts import render
from catalog.models import Product


def index(request):
    featured_products = Product.objects.all().prefetch_related("images")[:8]
    template_name = "pages/home.html"
    return render(request, template_name, {"featured_products": featured_products})


def login_view(request):
    return render(request, "pages/login.html")


def register_view(request):
    return render(request, "pages/register.html")
