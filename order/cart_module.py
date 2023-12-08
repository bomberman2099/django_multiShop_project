from product.models import Product

CART_SESSION_ID = 'cart'


class Cart:
    def __init__(self, request):
        # all of the user sessions on the self.session
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            # making the cart
            cart = self.session[CART_SESSION_ID] = {}

        self.cart = cart

    def __iter__(self):
        cart = self.cart.copy()
        for item in cart.values():
            product = Product.objects.get(id=int(item['id']))
            item['product'] = product
            item['total'] = int(item['price']) * int(item['quantity'])
            item['unique_id'] = self.Unique_id_generator(product.id, item['color'], item['size'])
            yield item

    def Unique_id_generator(self, id, color, size):
        result = f'{id}-{color}-{size}'
        return result

    def add(self, product, color, size, Quantity):
        # now we make the id for sessions
        unique = self.Unique_id_generator(product.id, color, size)
        if unique not in self.cart:
            # if the id is not on the session cart we create one
            print(product.id,2323232323323)
            self.cart[unique] = {'quantity': 0, 'price': str(product.price), 'color': color, 'size': size, 'id': str(product.id)}

        # the Quantity is a number. number of the Quantity.
        self.cart[unique]['quantity'] += int(Quantity)
        self.save()

    def total(self):
        cart = self.cart
        total = 0
        for item in cart.values():
            total += int(item['price'])
        return total

    def remove(self):
        del self.session[CART_SESSION_ID]
    def delete(self, id):
        if id in self.cart:
            del self.cart[id]
            self.save()
    def save(self):

        # for update
        self.session.modified = True
