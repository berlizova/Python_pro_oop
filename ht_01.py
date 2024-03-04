# Task 1
class Product:
    def __init__(self, category, name, price):
        self.category = category
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.category} - {self.name} - ${self.price}"


class Cart:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.basket = {}

    def add_to_cart(self, product, quantity):
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


# products
product1 = Product("food", "cucumbers", 2.50)
product2 = Product("equipment", "laptop", 2200)
product3 = Product("equipment", "headphones", 300.99)
product4 = Product("health", "vitamins", 15.99)
product5 = Product("beauty", "shampoo", 80.35)
product6 = Product("food", "tomatoes", 3.50)
product7 = Product("food", "meat", 7.00)

# carts
customer_cart1 = Cart("John Doe")
customer_cart2 = Cart("Jane Doe")

# add products
customer_cart1.add_to_cart(product3, 2)
customer_cart1.add_to_cart(product2, 1)
customer_cart1.add_to_cart(product7, 3)

customer_cart2.add_to_cart(product5, 2)
customer_cart2.add_to_cart(product6, 1)
customer_cart2.add_to_cart(product1, 3)
customer_cart2.add_to_cart(product4, 2)

print(customer_cart1)
print(customer_cart2)


# Task 2

class Dish:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.description} - ${self.price}"


class Menu:
    def __init__(self, name, dishes):
        self.name = name
        self.dishes = dishes

    def __str__(self):
        category_content = "\n".join([f"{dish}" for dish in self.dishes])
        return f"{self.name}:\n{category_content}"


# dishes
dish1 = Dish("Caesar Salad", "Fresh salad", 12.99)
dish2 = Dish("Spaghetti Bolognese", "Classic Italian pasta", 15.99)
dish3 = Dish("Chocolate Brownie", "Chocolate brownie", 7.99)
dish4 = Dish("Mozzarella Sticks", "Crispy mozzarella sticks", 8.99)
dish5 = Dish("Grilled Salmon", "Grilled salmon", 18.99)
dish6 = Dish("Tiramisu", "Classic Italian dessert", 9.99)

# menu categories
appetizers = MenuCategory("Appetizers", [dish1, dish4])
main_courses = MenuCategory("Main Courses", [dish2])
desserts = MenuCategory("Desserts", [dish3, dish6])
salads = MenuCategory("Salads", [dish1])
pasta = MenuCategory("Pasta", [dish2])
seafood = MenuCategory("Seafood", [dish5])

print("Restaurant Menu")
print(appetizers)
print(main_courses)
print(desserts)
print(salads)
print(pasta)
print(seafood)
