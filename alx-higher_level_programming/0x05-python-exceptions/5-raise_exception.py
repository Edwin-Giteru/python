def raise_exception():
    raise TypeError("This is a type exception")

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")
