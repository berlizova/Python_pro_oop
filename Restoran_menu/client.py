from discount import RegularDiscount, SilverDiscount, GoldDiscount


class Client:
    def __init__(self, name, discount):
        self.name = name
        self.discount = discount

    def get_total_price(self, order_total):
        discount_amount = self.discount.discount(order_total)
        total_price = order_total - discount_amount
        return total_price
