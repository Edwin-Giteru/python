# a class that a square that has size
#!/usr/bin/python3

class Square:
    def __init__(self,size):
        self._size = size
        
    
my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)