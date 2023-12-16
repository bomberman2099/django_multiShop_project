from django.shortcuts import render
from django.views.generic import TemplateView

from product.models import Product, Category


def Home(request):
    object_list = Product.objects.all()
    category = Category.objects.all()
    return render(request, 'home\index.html', context={'object_list': object_list, 'category': category})
