class Discount:
    def discount(self, order_total):
        pass


class RegularDiscount(Discount):
    def discount(self, order_total):
        return order_total * 0.1


class SilverDiscount(Discount):
    def discount(self, order_total):
        return order_total * 0.2


class GoldDiscount(Discount):
    def discount(self, order_total):
        return order_total * 0.35
