import random
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Execution time:", end_time - start_time, "seconds")
        return result
    return wrapper

@measure_time
def square_and_sum(numbers, func):
    result_list = [func(num) for num in numbers]
    return sum(result_list)

def square(x):
    return x ** 2

numbers = [random.randint(1, 10) for _ in range(5)]
print("Random numbers:", numbers)

result_sum = square_and_sum(numbers, square)
print("Sum of squared elements:", result_sum)
