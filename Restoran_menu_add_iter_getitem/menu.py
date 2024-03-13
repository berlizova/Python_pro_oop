import logging
from dish import Dish
from money_error import MoneyError

class Menu:
    def __init__(self, name, dishes):
        self.name = name
        self.dishes = dishes

    def __str__(self):
        category_content = "\n".join([f"{dish}" for dish in self.dishes])
        return f"{self.name}:\n{category_content}"

    def __iter__(self):
        return iter(self.dishes)

    def __len__(self):
        return len(self.dishes)

    def select_dishes(self):
        selected_dishes = []
        print(f"Please select dishes from the {self.name}:")
        while True:
            for i, dish in enumerate(self.dishes):
                print(f"{i + 1}. {dish}")
            print("Enter 0 to finish selecting dishes.")
            choice = int(input("Enter the number of the dish you want to add: "))
            if choice == 0:
                break
            selected_dishes.append(self.dishes[choice - 1])
        return selected_dishes

    def add_dish(self, dish):
        self.dishes.append(dish)
        logging.info(f"Added dish '{dish.name}' to the menu '{self.name}'")

    def remove_dish(self, dish):
        try:
            self.dishes.remove(dish)
            logging.info(f"Removed dish '{dish.name}' from the menu '{self.name}'")
        except ValueError:
            logging.error(f"Dish '{dish.name}' not found in the menu '{self.name}'")

    def check_prices(self):
        for dish in self.dishes:
            try:
                if dish.price <= 0:
                    logging.error(f"Invalid price {dish.price} for dish '{dish.name}' in the menu '{self.name}'")
                    raise MoneyError("Price must be a positive value")
            except MoneyError as e:
                print(e)


# Create instances of menus
appetizers = Menu("Appetizers", [
    Dish("Caesar Salad", "Fresh salad", 13.69),
    Dish("Mozzarella Sticks", "Crispy mozzarella sticks", 8.99)
])

main_courses = Menu("Main Courses", [
    Dish("Spaghetti Bolognese", "Classic Italian pasta", 15.99),
    Dish("Tomato Soup", "Classic Soup", 5.99)
])

desserts = Menu("Desserts", [
    Dish("Chocolate Brownie", "Chocolate brownie", 7.99),
    Dish("Tiramisu", "Classic Italian dessert", 9.99)
])

salads = Menu("Salads", [
    Dish("Caesar Salad", "Fresh salad", 12.99),
    Dish("Tomato Salad", "Fresh Tomato", 8.99)
])

pasta = Menu("Pasta", [
    Dish("Spaghetti Bolognese", "Classic Italian pasta", 15.99),
    Dish("Pizza", "Classic Italian Pizza", 15.99)
])

seafood = Menu("Seafood", [
    Dish("Grilled Salmon", "Grilled salmon", 18.99),
    Dish("Grilled pork", "Grilled pork", 9.99)
])
