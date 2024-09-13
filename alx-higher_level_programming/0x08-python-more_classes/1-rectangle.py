class Rectangle:
    def __init__(self, width=0, height=0):
        self._width  = width
        self.height = height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self,value):
        if not isinstance(value ,int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("Size must be >= 0 ")
        self._width = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,value):
        if not isinstance(value ,int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("Size must be >= 0 ")
        self._height = value

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)
