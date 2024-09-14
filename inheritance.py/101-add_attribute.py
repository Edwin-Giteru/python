def add_attribute(obj,name,value):
    if hasattr(obj,"__dict__"):
        setattr(obj,name,value)
    else:
        raise TypeError("Can't add new attribute")
    
class MyClass():
    pass

mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name)

try:
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))