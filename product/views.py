from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, ListView
from django.core.paginator import Paginator
from product.models import Product, Category, Size, Color


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
    paginate_by = 6
    model = Product
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data()
        context['size'] = Size.objects.all()
        context['color'] = Color.objects.all()

        selected_colors = self.request.GET.getlist('color')
        selected_sizes = self.request.GET.getlist('size')
        min_price = self.request.GET.get('min-price')
        max_price = self.request.GET.get('max-price')

        final_queryset = Product.objects.all()
        queryset = Product.objects.all()


        if selected_colors:
            queryset = Product.objects.filter(color__title__in=selected_colors).distinct()
        if selected_sizes:
            queryset = Product.objects.filter(size__title__in=selected_sizes).distinct()
        if min_price and max_price:
            queryset = Product.objects.filter(price__lte=max_price, price__gte=min_price)

        if selected_colors or selected_sizes or (min_price is not None and max_price is not None):
            final_queryset = Product.objects.none()

            if selected_colors:
                final_queryset = queryset.filter(color__title__in=selected_colors)

            if selected_sizes:
                final_queryset = final_queryset.filter(size__title__in=selected_sizes)

            if min_price is not None and max_price is not None:
                final_queryset = final_queryset.filter(price__range=(min_price, max_price))
        context['object_list'] = final_queryset.distinct()


        # print(selected_colors, selected_sizes, min_price, max_price)

        paginator = Paginator(queryset, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['object_list'] = page_obj
        context['selected_colors'] = selected_colors
        context['min_price'] = min_price
        context['max_price'] = max_price
        context['selected_sizes'] = selected_sizes
        context['page_obj'] = page_obj

        return context
