class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def __setattr__(self, name, value):
        if name in ['__width', '__height']:
            raise AttributeError("Cannot modify width or height directly")
        else:
            super().__setattr__(name, value)

    def __getattr__(self, name):
        return f"Property '{name}' does not exist"

    def area(self):
        return self.__width * self.__height


# Creating a rectangle object
rectangle = Rectangle(10, 50)

# Change the values directly
try:
    rectangle.width = 8
except AttributeError as e:
    print(e)

try:
    rectangle.height = 15
except AttributeError as e:
    print(e)

# Access a non-existent property
print(rectangle.something)

# Area of the rectangle
print("Area of the rectangle:", rectangle.area())
