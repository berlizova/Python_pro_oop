import re


def validate_bank_card(card_number):
    # Regular expression pattern for bank card number with optional spaces
    pattern = r'^\d{4}(?:[\s-]?\d{4}){3}$'

    # Check if the card number matches the pattern
    if re.match(pattern, card_number):
        return True
    else:
        return False


# Ask the user to input the card number
card_number = input("Enter the bank card number: ")

# Test the function
if validate_bank_card(card_number):
    print("Valid bank card number")
else:
    print("Invalid bank card number")
