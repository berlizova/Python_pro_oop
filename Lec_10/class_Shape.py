import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


class Pyramid(Shape):
    def __init__(self, base_length, base_width, height):
        self.base_length = base_length
        self.base_width = base_width
        self.height = height

    def area(self):
        base_area = self.base_length * self.base_width
        lateral_area = (self.base_length + self.base_width) * self.height / 2
        return base_area + lateral_area

    def perimeter(self):
        return "Perimeter not unsuitable for Pyramid"


# Creating objects of different shapes
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4, 5)
pyramid = Pyramid(4, 5, 6)

# Displaying area and perimeter of each shape
print("Circle:")
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())

print("\nRectangle:")
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())

print("\nTriangle:")
print("Area:", triangle.area())
print("Perimeter:", triangle.perimeter())

print("\nPyramid:")
print("Area:", pyramid.area())
print("Perimeter:", pyramid.perimeter())
