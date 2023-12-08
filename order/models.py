from django.db import models

from accounts.models import User
from product.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    creadted_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    total_price = models.IntegerField(default=0)
    def __str__(self):
        return self.user.phone



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    pruduct = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    size = models.CharField(max_length=12, null=True)
    color = models.CharField(max_length=12, null=True)
    quantity = models.SmallIntegerField()
    price = models.PositiveIntegerField()


    def __str__(self):
        return self.order.user.phone

class DiscountCode(models.Model):
    name = models.CharField(max_length=10, unique=True)
    discount = models.SmallIntegerField(default=0)
    quantity = models.SmallIntegerField(default=1)


    def __str__(self):
        return self.name