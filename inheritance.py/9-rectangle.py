class BaseGeometry:
    def area(self):
        raise Exception("area() not implemented")
    
    def integer_validator(self,name,value):
        self.name = name
        self.value = value

        if not isinstance(value,int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than zero")
        

class Rectangle(BaseGeometry):
    def __init__(self,width,height):
        self.integer_validator("width",width)
        self.integer_validator("height",height)

        self._width = width
        self._height = height

    def area(self):
        return self._height * self._width

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self._width,self._height))
    

r = Rectangle(3, 5)

print(r)
print(r.area())
