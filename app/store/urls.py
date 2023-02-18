from django.urls import path
from store.views.base import ProductsView
from store.views.product import ProductView, ProductAddView


urlpatterns = [
    path('', ProductsView.as_view(), name='index'),
    path('products', ProductsView.as_view(), name='products'),
    path('products/add', ProductAddView.as_view(), name='products_add')
    path('products/<int:pk>', ProductView.as_view(), name='products_detail'),
]
