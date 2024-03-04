class Discount:
    def discount(self, order_total):
        self: str
        order_total: float | int


class RegularDiscount(Discount):
    def discount(self, order_total):
        return order_total * 0.1


class SilverDiscount(Discount):
    def discount(self, order_total):
        return order_total * 0.2


class GoldDiscount(Discount):
    def discount(self, order_total):
        return order_total * 0.35


class Client:
    def __init__(self, name, discount):
        self.name = name
        self.discount = discount


    def get_total_price(self, order_total):
        discount_amount = self.discount.discount(order_total)
        total_price = order_total - discount_amount

        return total_price

#Discount
regular_discount = RegularDiscount()
silver_discount = SilverDiscount()
gold_discount = GoldDiscount()

client_regular = Client("John Doe", regular_discount)
client_silver = Client("Jane Doe", silver_discount)
client_gold = Client("Bob Doe", gold_discount)

order_total = 100.50  # Could be replaced
total_price_regular = client_regular.get_total_price(order_total)
total_price_silver = client_silver.get_total_price(order_total)
total_price_gold = client_gold.get_total_price(order_total)

print(f"{client_regular.name}'s total price: ${total_price_regular}")
print(f"{client_silver.name}'s total price: ${total_price_silver}")
print(f"{client_gold.name}'s total price: ${total_price_gold}")
