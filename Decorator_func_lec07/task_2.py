def square_and_sum(numbers, func):
    result_list = [func(num) for num in numbers]
    return sum(result_list)


def save_results_to_file(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Call the function
            result = func(*args, **kwargs)

            # Write result to file
            with open(filename, 'a') as file:
                file.write(str(result) + '\n')

            return result

        return wrapper

    return decorator


@save_results_to_file("results.txt")
def square(x):
    return x ** 2


numbers = [1, 2, 3, 4, 5]

result_sum = square_and_sum(numbers, square)
print("Sum of squared elements:", result_sum)
