#!/usr/bin/python3
class Rectangle:
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        self._width  = width
        self.height = height
        Rectangle.number_of_instances += 1   

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self,value):
        if not isinstance(value ,int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0 ")
        self._width = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,value):
        if not isinstance(value ,int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0 ")
        self._height = value

    def area(self):
        return self._width* self._height
    
    def perimeter(self):
        perimeter = 2 *(self._height + self._width)
        if self._height ==0 or self._width == 0:
            return 0
        
        return perimeter
    def __str__(self):
        
        if self._width == 0 or self._height == 0:
            return ""

        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += "#" * self.width +"\n"
        return rectangle_str
    
    def __repr__(self):
        return "Rectangle ({},{})".format(self.width,self.height)


    def __del__(self):
        print("Bye triangle...")
        Rectangle.number_of_instances -= 1

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
