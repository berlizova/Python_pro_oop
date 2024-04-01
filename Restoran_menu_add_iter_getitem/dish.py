import logging
from money_error import MoneyError

class Dish:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self._price = None  # Initialize price attribute to None
        self.price(price)  # Use the combined method to set price

    def price(self, value=None):
        if value is not None:
            if value <= 0:
                logging.error(f"Invalid price {value} for dish {self.name}")
                raise MoneyError("Price must be a positive value")
            self._price = value
        return self._price

    def __str__(self):
        return f"{self.name} - {self.description} - ${self._price}"
