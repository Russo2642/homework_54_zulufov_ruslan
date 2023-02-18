from django.urls import path
from store.views.base import ProductsView
from store.views.product import ProductView, ProductAddView, ProductEditView, ProductDeleteView
from store.views.category import CategoryView, CategoryAddView


urlpatterns = [
    path('', ProductsView.as_view(), name='index'),
    path('products/', ProductsView.as_view(), name='products'),
    path('products/add', ProductAddView.as_view(), name='product_add'),
    path('products/<int:pk>', ProductView.as_view(), name='product_detail'),
    path('products/<int:pk>/edit', ProductEditView.as_view(), name='product_edit'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('categories/add', CategoryAddView.as_view(), name='category_add'),
    path('categories/', CategoryView.as_view(), name='categories'),
]
