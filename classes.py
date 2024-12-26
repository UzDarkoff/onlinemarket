class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def str(self):
        return f"{self.product_id}. {self.name} - {self.price} so'm"


class Cart:
    def __init__(self):
        self.items = {}

    def add_to_cart(self, product, quantity):
        if product.product_id in self.items:
            self.items[product.product_id]['quantity'] += quantity
        else:
            self.items[product.product_id] = {'product': product, 'quantity': quantity}

    def remove_from_cart(self, product_id):
        if product_id in self.items:
            del self.items[product_id]

    def view_cart(self):
        if not self.items:
            return "Savatchangiz bo'sh."
        result = "Savatchangiz:\n"
        total = 0
        for item in self.items.values():
            product = item['product']
            quantity = item['quantity']
            cost = product.price * quantity
            total += cost
            result += f"{product.name} - {quantity} ta - {cost} so'm\n"
        result += f"Umumiy summa: {total} so'm"
        return result


class Order:
    def __init__(self):
        self.orders = []

    def place_order(self, cart):
        if not cart.items:
            return "Savatchangiz bo'sh, buyurtma bera olmaysiz."
        self.orders.append(cart.items.copy())
        cart.items.clear()
        return "Buyurtmangiz muvaffaqiyatli qabul qilindi!"

