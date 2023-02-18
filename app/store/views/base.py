from django.shortcuts import render
from django.views import View
from store.models import Product


class ProductsView(View):
    def get(self, request):
        product = Product.objects.all()
        context = {
            'product': product
        }
        return render(request, 'index.html', context=context)
