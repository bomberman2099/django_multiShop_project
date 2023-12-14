from django.urls import path
from . import views


app_name = 'product'
urlpatterns = [
    path('detail/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('navbar', views.NavbarePartialView.as_view(), name='navbar'),
    path('sample', views.SampleCategoryView.as_view(), name='sample_category'),
    path('list', views.ProductListView.as_view(), name='product_list'),
]