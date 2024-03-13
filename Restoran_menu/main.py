from dish import Dish
from menu import Menu
from order import Order
from discount import RegularDiscount, SilverDiscount, GoldDiscount
from menu import appetizers, main_courses, desserts, salads, pasta, seafood

# Assuming you have defined appetizers, main_courses, desserts, salads, pasta, and seafood objects
menus = [appetizers, main_courses, desserts, salads, pasta, seafood]

def select_dishes(menu):
    print(f"Please select dishes from the {menu.name}:")
    selected_dishes = []
    while True:
        for i, dish in enumerate(menu.dishes):
            print(f"{i + 1}. {dish}")
        print("Enter 0 to finish selecting dishes.")
        choice = int(input("Enter the number of the dish you want to add: "))
        if choice == 0:
            break
        selected_dishes.append(menu.dishes[choice - 1])
    return selected_dishes

def calculate_total_with_discount(order_total, client_discount):
    return order_total - client_discount.discount(order_total)

print("Welcome to the restaurant!")

# Select menu
print("Please select a menu:")
for i, menu in enumerate(menus):
    print(f"{i + 1}. {menu.name}")
menu_choice = int(input("Enter the number of the menu you want to view: "))
selected_menu = menus[menu_choice - 1]

# Display selected menu and select dishes
selected_dishes = select_dishes(selected_menu)

# Create order and add selected dishes
order = Order()
for dish in selected_dishes:
    order.add_item(dish)

# Calculate total price
order_total = order.calculate_total()

# Select discount level
discount_levels = {
    1: RegularDiscount(),
    2: SilverDiscount(),
    3: GoldDiscount()
}
print("Select your discount level:")
print("1. Regular")
print("2. Silver")
print("3. Gold")
discount_choice = int(input("Enter the number of your discount level: "))
client_discount = discount_levels.get(discount_choice)

# Calculate total price with discount
total_with_discount = calculate_total_with_discount(order_total, client_discount)

print(f"Your total price with discount: ${total_with_discount}")
