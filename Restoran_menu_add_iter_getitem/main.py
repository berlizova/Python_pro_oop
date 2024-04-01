from dish import Dish
from menu import appetizers, main_courses, desserts, salads, pasta, seafood
from order_getitem_len_next import Order
from discount import RegularDiscount, SilverDiscount, GoldDiscount


def select_category():
    print("Please select a category:")
    print("1. Appetizers")
    print("2. Main Courses")
    print("3. Desserts")
    print("4. Salads")
    print("5. Pasta")
    print("6. Seafood")
    print("0. Finish ordering")

    category_choice = int(input("Enter the number of the category you want to order from: "))
    return category_choice


def select_dish(menu):
    print(f"Please select a dish from {menu.name}:")
    while True:
        for i, dish in enumerate(menu.dishes):
            print(f"{i + 1}. {dish}")
        print("Enter 0 to finish selecting dishes from this category.")
        dish_choice = int(input("Enter the number of the dish you want to add: "))
        if dish_choice == 0:
            break
        yield menu.dishes[dish_choice - 1]


def calculate_total_with_discount(order_total, client_discount):
    return order_total - client_discount.discount(order_total)


print("Welcome to the restaurant!")

# Create a new order
order = Order()

# Select dishes from different categories
while True:
    category_choice = select_category()
    if category_choice == 0:
        break

    selected_menu = None
    if category_choice == 1:
        selected_menu = appetizers
    elif category_choice == 2:
        selected_menu = main_courses
    elif category_choice == 3:
        selected_menu = desserts
    elif category_choice == 4:
        selected_menu = salads
    elif category_choice == 5:
        selected_menu = pasta
    elif category_choice == 6:
        selected_menu = seafood
    else:
        print("Invalid category choice!")
        continue

    selected_dishes = select_dish(selected_menu)
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
