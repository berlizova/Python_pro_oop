import logging

class MoneyError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return f"MoneyError: {self.message}"

class Dish:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self._price = None  # Initialize price attribute to None
        self.set_price(price)  # Use setter method to set price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self.set_price(value)

    def set_price(self, value):
        if value <= 0:
            logging.error(f"Invalid price {value} for dish {self.name}")
            raise MoneyError("Price must be a positive value")
        self._price = value

    def __str__(self):
        return f"{self.name} - {self.description} - ${self.price}"
