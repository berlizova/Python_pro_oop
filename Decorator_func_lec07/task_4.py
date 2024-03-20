def square_and_sum(numbers, func):
    result_list = [func(float(num)) for num in numbers.split(',')]
    return sum(result_list)


def square(x):
    return x ** 2


numbers = input('write the number( ex: 1,2,3) :')

result_sum = square_and_sum(numbers, square)
print("Sum of squared elements:", result_sum)
