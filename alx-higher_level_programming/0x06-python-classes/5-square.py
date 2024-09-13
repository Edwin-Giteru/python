# A class that prints a square as #
#!/usr/bin/python3

class Square:
    def __init__(self,size=0):
        self._size = size

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self,value):
        if not isinstance(value,int):
            raise TypeError("Size must be an integer")
        if value < 0:
            raise ValueError("Size must be >= 0")
        
    def area(self):
        return self.size**2
    
    def my_print(self):
        if self._size ==0:
            print("")
        else:
            for _ in range(self._size):
                print("#" * self._size)

my_square = Square(3)
my_square.my_print()
print("_ _")

my_square = Square(10)
my_square.my_print()
print("_ _")

my_square = Square(0)
my_square.my_print()
print("_ _")

