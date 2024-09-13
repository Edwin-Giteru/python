#!/usr/bin/python3
class Rectangle:
    number_of_instances = 0
    print_symbol = "#"
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
            rectangle_str += str(self.print_symbol) * self.width +"\n"
        return rectangle_str
    
    def __repr__(self):
        return "Rectangle ({},{})".format(self.width,self.height)


    def __del__(self):
        print("Bye triangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1,Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        
        elif not isinstance(rect_2,Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
        
        
my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")


my_rectangle_2.width = 10
my_rectangle_2.height = 5
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")