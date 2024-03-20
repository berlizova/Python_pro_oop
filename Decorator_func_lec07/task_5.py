def limit_calls(max_calls):
    def decorator(func):
        calls = 0

        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls < max_calls:
                calls += 1
                return func(*args, **kwargs)
            else:
                raise StopIteration("Maximum number of function calls reached.")

        return wrapper

    return decorator


@limit_calls(5)
def square_and_sum(numbers, func):
    result_list = [func(float(num)) for num in numbers.split(',')]
    return sum(result_list)


def square(x):
    return x ** 2


while True:
    try:
        numbers = input('Write the numbers (ex: 1,2,3): ')
        result_sum = square_and_sum(numbers, square)
        if result_sum is not None:
            print("Sum of squared elements:", result_sum)
    except StopIteration as e:
        print(e)
        break
