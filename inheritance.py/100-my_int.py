class MyInt(int):
    def __eq__(self, __value: object) -> bool:
        return super().__ne__(__value)
    
    def __ne__(self, __value: object) -> bool:
        return super().__eq__(__value)
my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)