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

        discount = GoldDiscount()
        order_1 = Order("Jon", "Doe", cart_1, discount)
        discount = SilverDiscount()
        order_2 = Order("Jane", "Doe", cart_2, discount)

        # Combining carts using the += operator
        combined_cart = Cart()
        combined_cart += cart_1
        combined_cart += cart_2

        #print("Combined Cart:")
        #print(combined_cart)

        discount = GoldDiscount()
        combined_order = Order("Combined", "Order", combined_cart, discount)

        print(f'Jon', order_1)
        print(f'Jane', order_2)
        print(f'Combined', combined_order)
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