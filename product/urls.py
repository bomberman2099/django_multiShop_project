from django.urls import path
from . import views


app_name = 'product'
urlpatterns = [
    path('detail/<int:pk>', views.ProductDetailView.as_view(), name='product_detail')
]