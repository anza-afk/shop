class Cart():

    def __init__(self, request) -> None:
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        if product.id not in self.cart:
            self.cart[product.id] = quantity
        if update_quantity:
            self.cart[product.id] = quantity
        else:
            self.cart[product.id] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        if product.id in self.cart:
            del self.cart[product.id]
            self.save()
