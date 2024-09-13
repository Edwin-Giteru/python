class Square:
    def __init__(self,size):
        self._size = size
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self,new_size):
        if not isinstance(new_size,int):
            raise TypeError("Size must be an integer")
        if new_size < 0:
            raise ValueError("Size must be > = 0")
    def area(self):
        return self._size**2

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)
   
