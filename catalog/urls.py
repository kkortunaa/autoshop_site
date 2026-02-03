from django.urls import path

from . import views

urlpatterns = [
    path('<int:product_id>/', views.product_detail_view, name='product_detail'),
    path('', views.catalog_view, name='catalog')
] 