from dish import Dish

class Menu:
    def __init__(self, name, dishes):
        self.name = name
        self.dishes = dishes

    def __str__(self):
        category_content = "\n".join([f"{dish}" for dish in self.dishes])
        return f"{self.name}:\n{category_content}"

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


# Create instances of menus
appetizers = Menu("Appetizers", [
    Dish("Caesar Salad", "Fresh salad", 12.99),
    Dish("Mozzarella Sticks", "Crispy mozzarella sticks", 8.99)
])

main_courses = Menu("Main Courses", [
    Dish("Spaghetti Bolognese", "Classic Italian pasta", 15.99)
])

desserts = Menu("Desserts", [
    Dish("Chocolate Brownie", "Chocolate brownie", 7.99),
    Dish("Tiramisu", "Classic Italian dessert", 9.99)
])

salads = Menu("Salads", [
    Dish("Caesar Salad", "Fresh salad", 12.99)
])

pasta = Menu("Pasta", [
    Dish("Spaghetti Bolognese", "Classic Italian pasta", 15.99)
])

seafood = Menu("Seafood", [
    Dish("Grilled Salmon", "Grilled salmon", 18.99)
])
