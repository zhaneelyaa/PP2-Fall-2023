class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


length = float(input("Enter the length: "))
width = float(input("Enter the width (for rectangle): "))


square = Square(length)
rectangle = Rectangle(length, width)


print("Square area is:", square.area())
print("Rectangle area is:", rectangle.area())
