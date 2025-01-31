class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity=1):
        if price < 0 or quantity < 1:
            raise ValueError("Ungültiger Preis oder Menge")
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def total_price(self):
        return sum(item["price"] * item["quantity"] for item in self.items)

    def remove_item(self, name):
        self.items = [item for item in self.items if item["name"] != name]

    def clear_cart(self):
        self.items = []
