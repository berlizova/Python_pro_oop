#Task 1
class MoneyError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return f"MoneyError: {self.message}"


class Product:
    def __init__(self, category, name, price):
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number.")
        if price <= 0:
            raise MoneyError("Price cannot be negative.")

        self.category = category
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"{self.category} - {self.name} - ${self.price}"


class Cart:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.basket = {}

    def add_to_cart(self, product, quantity):
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer")

        if product in self.basket:
            self.basket[product] += quantity
        else:
            self.basket[product] = quantity

    def calc_cart_value(self):
        total_value = 0
        for product, quantity in self.basket.items():
            total_value += product.price * quantity
        return total_value

    def __str__(self):
        cart_content = "\n".join([f"{product} - Quantity: {quantity}" for product, quantity in self.basket.items()])
        return f"Customer: {self.customer_name}\nCart Content:\n{cart_content}\nTotal Value: ${self.calc_cart_value()}"


# Example usage:

# products
product1 = Product("food", "cucumbers", 15.70)
product2 = Product("equipment", "laptop", 2200)
product3 = Product("equipment", "headphones", 300.99)
product4 = Product("health", "vitamins", 15.99)
product5 = Product("beauty", "shampoo", 80.35)
product6 = Product("food", "tomatoes", 3.50)
product7 = Product("food", "meat", 7.00)

# carts
customer_cart1 = Cart("John Doe")
customer_cart2 = Cart("Jane Doe")

try:
    # add products
    customer_cart1.add_to_cart(product3, 2)
    customer_cart1.add_to_cart(product2, -5)
    customer_cart1.add_to_cart(product7, 3)

    customer_cart2.add_to_cart(product5, 2)
    customer_cart2.add_to_cart(product6, 1)
    customer_cart2.add_to_cart(product1, 3)
    customer_cart2.add_to_cart(product4, 2)

    print(customer_cart1)
    print(customer_cart2)

except MoneyError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
