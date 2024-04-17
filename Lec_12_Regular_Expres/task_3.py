import re


def validate_email(email):
    # Regular expression pattern for email validation
    pattern = r'^[a-zA-Z0-9]+([_\-.][a-zA-Z0-9]+)*@[a-zA-Z0-9]+([_\-.][a-zA-Z0-9]+)*\.[a-zA-Z]{2,}$'

    # Check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False


# Test the function
email = input("Enter an email address: ")

if validate_email(email):
    print("Valid email address")
else:
    print("Invalid email address")
