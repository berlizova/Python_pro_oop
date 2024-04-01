class Account:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def __setattr__(self, name, value):
        if name == '_Account__balance':
            raise AttributeError("Cannot modify balance directly")
        else:
            super().__setattr__(name, value)

    def __getattr__(self, name):
        return f"Property '{name}' does not exist"


# Creating an account object
acc = Account(1000)

# Change the balance directly
try:
    acc.balance = 2000
except AttributeError as e:
    print(e)

# Access a non-existent property
print(acc.something)
