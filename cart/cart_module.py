from decimal import Decimal


class Cart:
    SESSION_KEY = "cart"

    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get(self.SESSION_KEY)

        if self.cart is None:
            self.cart = {}
            self.session[self.SESSION_KEY] = self.cart

    def save(self):
        self.session[self.SESSION_KEY] = self.cart
        self.session.modified = True

    def generate_key(self, product_id, size, color):
        return f"{product_id}_{size}_{color}"

    def add(self, product, size, color, quantity=1):

        key = self.generate_key(product.id, size, color)

        if key not in self.cart:
            self.cart[key] = {
                "product_id": product.id,
                "title": product.title,
                "price": str(product.price),
                "image": product.image.url,
                "size": size,
                "color": color,
                "quantity": 0,
            }

        self.cart[key]["quantity"] += quantity

        self.save()

    def update(self, key, quantity):

        if key in self.cart:

            if quantity <= 0:
                del self.cart[key]
            else:
                self.cart[key]["quantity"] = quantity

            self.save()

    def remove(self, key):

        if key in self.cart:
            del self.cart[key]
            self.save()

    def clear(self):

        self.session[self.SESSION_KEY] = {}
        self.session.modified = True

    def get_items(self):

        items = []

        for key, item in self.cart.items():

            subtotal = Decimal(item["price"]) * item["quantity"]

            items.append({
                "key": key,
                "product_id": item["product_id"],
                "title": item["title"],
                "price": Decimal(item["price"]),
                "image": item["image"],
                "size": item["size"],
                "color": item["color"],
                "quantity": item["quantity"],
                "subtotal": subtotal,
            })

        return items

    def get_total_price(self):

        total = Decimal("0")

        for item in self.cart.values():
            total += Decimal(item["price"]) * item["quantity"]

        return total

    def get_total_quantity(self):

        return sum(item["quantity"] for item in self.cart.values())