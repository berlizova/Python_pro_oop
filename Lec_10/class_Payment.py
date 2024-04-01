class PaymentInstrument:
    def make_payment(self, amount):
        raise NotImplementedError("make_payment method must be implemented in subclasses")


class CreditCard(PaymentInstrument):
    def make_payment(self, amount):
        print(f"Payment of ${amount} made using Credit Card")


class BankTransfer(PaymentInstrument):
    def make_payment(self, amount):
        print(f"Payment of ${amount} made via Bank Transfer")


class ElectronicWallet(PaymentInstrument):
    def make_payment(self, amount):
        print(f"Payment of ${amount} made using Electronic Wallet")


class PaymentProcessor:
    def __init__(self):
        self.available_methods = {}

    def add_payment_method(self, name, payment_method):
        self.available_methods[name] = payment_method

    def make_payment(self, method_name, amount):
        if method_name in self.available_methods:
            payment_method = self.available_methods[method_name]
            payment_method.make_payment(amount)
        else:
            print(f"Error: {method_name} is not available as a payment method")


# Example usage:
if __name__ == "__main__":
    processor = PaymentProcessor()

    # Adding payment methods
    processor.add_payment_method("Credit Card", CreditCard())
    processor.add_payment_method("Bank Transfer", BankTransfer())
    processor.add_payment_method("Electronic Wallet", ElectronicWallet())

    # Making payments
    processor.make_payment("Credit Card", 100)
    processor.make_payment("Bank Transfer", 200)
    processor.make_payment("Electronic Wallet", 300)
    processor.make_payment("PayPal", 75)  # Non-existing
