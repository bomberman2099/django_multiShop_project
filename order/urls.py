from django.urls import path
from . import views
app_name = 'order'
urlpatterns = [
    path('order/', views.OrderingView.as_view(), name='order'),
    path('add/<int:pk>', views.OrderADdDetail.as_view(), name='add_order'),
    path('delete/<str:id>', views.OrderDeleteView.as_view(), name='delete_order'),
    path('order/<int:pk>', views.OrderDetailView.as_view(), name='detail_order'),
    path('create/order', views.OrderCreationView.as_view(), name='create_order'),
    path('applydiscount/<int:pk>', views.ApplyDiscountView.as_view(), name='apply_discount'),

]