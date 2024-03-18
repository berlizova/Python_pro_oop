def to_cube(numbers):
    return (num ** 3 for num in numbers)


# Input
value = int(input("Enter the value: "))


cubes_list = list(to_cube(range(2, value + 1)))

# Cube List
print("List of cubes:")
print(cubes_list)
