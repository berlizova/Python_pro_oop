def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_generator(upper_limit):
    num = 2
    while num <= upper_limit:
        if is_prime(num):
            yield num
        num += 1


upper_limit = int(input("Enter the upper limit for prime numbers: "))
print(f"Prime numbers up to {upper_limit}:")
for prime in prime_generator(upper_limit):
    print(prime, end=" ")
