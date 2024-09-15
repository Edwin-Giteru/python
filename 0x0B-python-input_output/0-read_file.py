def read_file(filename=""):
    with open(filename,"r",encoding="utf-8") as f:
        print(f.read(),end="")
    
read_file("100-my_int.py")
