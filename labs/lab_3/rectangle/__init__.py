"""
Write a Rectangle class in Python language, allowing you to build a rectangle 
with length and width attributes.
Create a Perimeter() method to calculate the perimeter of the rectangle 
and Area() method to calculate the area of the rectangle.
Create a method display() that display the length, width, perimeter and area of an 
object created using an instantiation on rectangle class.
Create a Parallelepipede child class inheriting from the Rectangle class and with 
a height attribute and another Volume () method to calculate the volume of 
the Parallelepiped
"""

class Rectangle:
    length: float
    width: float

    def __init__(self, l, w):
        self.length = l
        self.width = w

    def __repr__(self):
        data_dict = {
            'length': self.length,
            'width': self.width,
            'perimeter': self.perimeter(),
            'area': self.area(),
        }
        return f"Rectangle: {data_dict}"

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.length * self.width)
