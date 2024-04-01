class User:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    def __setattr__(self, name, value):
        if name in ['_first_name', '_last_name']:
            raise AttributeError("Cannot modify first_name or last_name directly")
        else:
            super().__setattr__(name, value)

    def __getattr__(self, name):
        return f"Property '{name}' does not exist"


# User
user = User("Jon", "Doe")

# Change the first_name directly
try:
    user.first_name = "Jane"
except AttributeError as e:
    print(e)

# Access a non-existent property
print(user.something)
