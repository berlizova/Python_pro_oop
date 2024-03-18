def custom_range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0

    while (step > 0 and start < stop) or (step < 0 and start > stop):
        yield start
        start += step


# User inputs
try:
    start = int(input("Enter the start number: "))
    stop = int(input("Enter the stop number: "))
    step = int(input("Enter the step value: "))
except ValueError:
    print("Invalid input! Please enter integers.")
else:

    print(f"Using custom_range({start}, {stop}, {step}):")
    for i in custom_range(start, stop, step):
        print(i, end=" \n")
