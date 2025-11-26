class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (3.14 * (self.radius ** 2))

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return (self.length * self.breadth)

class Triangle(Shape):
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def area(self):
        return ((self.base * self.height)/2)

circle = Circle(7)
print(circle.area())

rectangle = Rectangle(5, 4)
print(rectangle.area())

triangle = Triangle(10, 5)
print(triangle.area())