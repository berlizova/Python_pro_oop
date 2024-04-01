import math

class Rational:
    def __init__(self, numerator: int, denominator: int):
        if not isinstance(numerator, int):
            raise TypeError('Numerator must be an integer')
        if not isinstance(denominator, int):
            raise TypeError('Denominator must be an integer')
        if denominator == 0:
            raise ZeroDivisionError('Denominator must not be zero')
        if denominator < 0:
            raise ValueError('Denominator must be positive')

        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __add__(self, other):
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __sub__(self, other):
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)


if __name__ == "__main__":
    a = Rational(1, 2)
    b = Rational(-2, 3)

    print("a =", a)
    print("b =", b)

    print("a == r2:", a == b)
    print("a < r2:", a < b)
    print("a + r2 =", a + b)
    print("a - r2 =", a - b)
    print("a * r2 =", a * b)
