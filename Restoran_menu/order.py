from dish import Dish


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, dish):
        self.items.append(dish)

    def calculate_total(self):
        total = sum([dish.price for dish in self.items])
        return total
