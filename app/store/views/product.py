from django.views import View
from django.views.generic.edit import UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from store.models import Product, Category


class ProductView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'product.html', context={
            'product': product
        })


class ProductAddView(View):
    def get(self, request):
        category = Category.objects.all()
        return render(request, 'product_create.html', context={'category': category})

    def post(self, request):
        product_data = {
            'title': request.POST.get('title'),
            'description': request.POST.get('description'),
            'category': Category.objects.get(id=request.POST.get('category')),
            'price': request.POST.get('price'),
            'image': request.POST.get('image'),
        }
        product = Product.objects.create(**product_data)
        reverse_url = reverse('product_detail', kwargs={'pk': product.pk})
        return redirect(reverse_url)


class ProductEditView(UpdateView):
    model = Product
    template_name = 'update_product.html'
    fields = [
        "title",
        "price",
        "image",
        'category',
        "description",
    ]
    success_url = "/"


class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/'
    template_name = "product.html"
