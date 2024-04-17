import re


def validate_login(login):
    # Regular expression pattern for login validation
    pattern = r'^[a-zA-Z0-9]{2,10}$'

    # Check if the login matches the pattern
    if re.match(pattern, login):
        return True
    else:
        return False


# Test the function
login = input("Enter a login: ")

if validate_login(login):
    print("Valid login")
else:
    print("Invalid login")
