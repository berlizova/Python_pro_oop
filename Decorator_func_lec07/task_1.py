def square_and_sum(numbers, func):
    result_list = [func(num) for num in numbers]
    return sum(result_list)


def square(x):
    return x ** 2


numbers = [1, 2, 3, 4, 6]

result_sum = square_and_sum(numbers, square)
print("Sum of squared elements:", result_sum)
