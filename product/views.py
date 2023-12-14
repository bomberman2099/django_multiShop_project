from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, ListView

from product.models import Product, Category


class ProductDetailView(DetailView):
    template_name = 'product/detail.html'
    model = Product


class NavbarePartialView(TemplateView):
    template_name = 'includes/navbar.html'

    def get_context_data(self, **kwargs):
        contex = super(NavbarePartialView, self).get_context_data()  # super for get_contex_data
        contex['categories'] = Category.objects.all()
        return contex


class SampleCategoryView(TemplateView):
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        contex = super(SampleCategoryView, self).get_context_data()
        contex['categories'] = Category.objects.all()
        return contex


class ProductListView(ListView):
    template_name = 'product/shop.html'
    queryset = Product.objects.all()

