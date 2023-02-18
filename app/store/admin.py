from django.contrib import admin

from store.models import Category, Product


# Register your models here.
@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'price', 'created_at', 'updated_at')
