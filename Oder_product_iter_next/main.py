from product import Product
from cart import Cart
from discount import GoldDiscount, SilverDiscount
from order import Order
from user_exceptions import PriceError

if __name__ == '__main__':
    try:
        p1 = Product("Headset", 500)
        p2 = Product("Laptop", 2500)
        p3 = Product("Phone", 1500)
        p4 = Product("Smartwatch", 700)

        cart_1 = Cart()
        cart_1.add_product(p1, 3)
        cart_1.add_product(p2, 1)
        cart_1.add_product(p3, 2)
        cart_1.add_product(p4, 4)

        cart_2 = Cart()
        cart_2.add_product(p1, 1)
        cart_2.add_product(p2, 1)
        cart_2.add_product(p3, 3)
        cart_2.add_product(p4, 2)

        # Iterating through products in cart_1
        print("Products in cart_1:")
        for item, quantity in cart_1:
            print(f"{item.name}: {quantity}")

        # Iterating through products in cart_2
        print("\nProducts in cart_2:")
        for item, quantity in cart_2:
            print(f"{item.name}: {quantity}")

        # Your remaining code...
    except PriceError as pe:
        print(f"PriceError: {pe}")
    except TypeError as te:
        print(f"TypeError: {te}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"Exception: {e}")
    finally:
        print("Done")