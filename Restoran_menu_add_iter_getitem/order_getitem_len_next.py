from dish import Dish


class Order:
    def __init__(self):
        self.items = []
        self._index = 0

    def add_item(self, dish):
        self.items.append(dish)

    def calculate_total(self):
        total = sum([dish.price for dish in self.items])
        return total

    def __iter__(self):
        return iter(self.items)

    def __next__(self):
        if self._index < len(self.items):
            item = self.items[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

    def __getitem__(self, index):
        return self.items[index]

    def __len__(self):
        return len(self.items)
