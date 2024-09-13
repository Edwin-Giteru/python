# A class to show the coordinates of a square
#!/usr/bin/python3


class Square:
    def __init__(self,size = 0,position=(0,0)):
        self._size = size
        self._position = position

    @property
    def size(self):
        return self._size
    
    @property
    def size(self,value):
        if not isinstance(value,int):
            raise TypeError("Size must be an integer")
        if value < 0:
            raise ValueError("Size must be >=0")
    
    @property
    def position(self):
        return self._position
    
    @property
    def size(self,value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        return self.size ** 2
    
    def my_print(self):
        if self._size < 0:
            print("_ _")
        
        for _ in range(self._position[1]):
            print("")

        # Print each row of the square
        for _ in range(self._size):
            # Print leading spaces based on position[0] and then the '#' symbols
            print(" " * self._position[0] + "#" * self._size)

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")

        
