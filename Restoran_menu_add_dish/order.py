from dish import Dish

class Order:
    def __init__(self):
        self.items = []

    def __iadd__(self, dish):
        if isinstance(dish, Dish):
            self.items.append(dish)
        else:
            raise TypeError("Only Dish objects can be added to an Order")
        return self

    def add_item(self, dish):
        self.items.append(dish)

    def calculate_total(self):
        total = sum([dish.price for dish in self.items])
        return total
