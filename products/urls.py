from django.urls import path
from .views import create_product, get_products, product_index

urlpatterns = [
    path('create/', create_product, name='create_product'),
    path('list/', get_products, name='get_products'),
    path('', product_index, name='product_index'),
]

