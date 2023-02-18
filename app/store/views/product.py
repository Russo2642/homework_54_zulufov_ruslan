from django.views import View
from django.views.generic.edit import UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from store.models import Product

class ProductView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'product.html', context={
            'product': product
        })


class ProductAddView(View):
    def get(self, request):
        return render(request, 'product_create.html')

    def post(self, request):
        product_data = {
            'title': request.POST.get('title'),
            'description': request.POST.get('description'),
            'category': request.POST.get('category'),
            'price': request.POST.get('price'),
            'image': request.POST.get('image')
        }
        product = Product.objects.create(**product_data)
        reverse_url = reverse('product_detail', kwargs={'pk': product.pk})
        return redirect(reverse_url)
