from django.views import View
from django.views.generic.edit import UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from store.models import Category


class CategoryView(View):
    def get(self, request):
        category = Category.objects.all()
        context = {
            'category': category
        }
        return render(request, 'category.html', context=context)


class CategoryAddView(View):
    def get(self, request):
        return render(request, 'category_create.html')

    def post(self, request):
        category_data = {
            'title': request.POST.get('title'),
            'description': request.POST.get('description')
        }
        category = Category.objects.create(**category_data)
        return redirect('/categories/')


class CategoryEditView(UpdateView):
    model = Category
    template_name = 'update_category.html'
    fields = [
        "title",
        "description"
    ]
    success_url = "/"


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/'
    template_name = "category.html"
