from product import Product


class Cart:

    def __init__(self):
        self.__items = []
        self.__quantities = []
        self.__index = 0


    def add_product(self, item: Product, quantity=1):
        if not isinstance(item, Product):
            raise TypeError("item must be a Product")
        if not isinstance(quantity, int | float):
            raise TypeError("Quantity must be a number")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        self.__items.append(item)
        self.__quantities.append(quantity)


    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index < len(self.__items):
            item = self.__items[self.__index]
            quantity = self.__quantities[self.__index]
            self.__index+= 1
            return item, quantity
        else:
            raise StopIteration


    def __iadd__(self, other):
        if not isinstance(other, Cart):
            raise TypeError("Can only combine with another Cart")

        self.__items.extend(other.__items)
        self.__quantities.extend(other.__quantities)
        return self

    def total(self):
        return sum(item.price * quantity for item, quantity in zip(self.__items, self.__quantities))

    def __str__(self):
        items = "\n".join([f"{item.name}: {quantity}" for item, quantity in zip(self.__items, self.__quantities)])
        return f"Cart with: \n{items}\nTotal: {self.total()}"