from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView

from order.cart_module import Cart
from order.models import Order, OrderItem, DiscountCode
from product.models import Product


class OrderingView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'order/ordering.html', {'cart': cart})


class OrderADdDetail(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        size, color, Quantity = request.POST.get('size'), request.POST.get('color'), request.POST.get('Quantity')
        print(size, color, Quantity)
        # we create the module for session cart in the cart_module.py
        cart = Cart(request)  # this class create a session with name cart

        cart.add(product, color, size, Quantity)
        return redirect('order:order')


class OrderDeleteView(View):
    def get(self, request, id):
        cart = Cart(request)
        cart.delete(id)
        return redirect('order:order')


class OrderDetailView(View):
    def get(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        return render(request, 'order/order_detail.html', {"order": order})


class OrderCreationView(View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user, total_price=int(cart.total()))
        for item in cart:
            OrderItem.objects.create(order=order, pruduct=item['product'], size=item['size'], color=item['color'],
                                     quantity=item['quantity'], price=item['price'])

        cart.remove()
        return redirect('order:detail_order', order.id)


class ApplyDiscountView(View):
    def post(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        code = request.POST.get('discount_code')
        discount_code = get_object_or_404(DiscountCode, name=code)
        if discount_code.quantity == 0:
            return redirect('order:detail_order')
        order.total_price -= order.total_price * discount_code.discount/100
        order.save()
        discount_code.quantity -= 1
        discount_code.save()
        return redirect('order:detail_order', order.id)
