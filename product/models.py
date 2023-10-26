from django.db import models


class Size(models.Model):
    title = models.CharField(max_length=10)


    def __str__(self):
        return self.title
class Color(models.Model):
    title = models.CharField(max_length=10)


    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=35)
    description = models.TextField()
    price = models.IntegerField(default=100000)
    discount = models.SmallIntegerField(blank=True, null=True, default=0)
    image = models.ImageField(upload_to='products')
    size = models.ManyToManyField(Size, blank=True, null=True, related_name='products')
    color = models.ManyToManyField(Color, related_name='colors')

    def __str__(self):
        return self.title