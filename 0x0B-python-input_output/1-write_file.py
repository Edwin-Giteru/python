def write_file(filename="",text=""):
    with open(filename,"w",encoding="utf-8") as f:
        print(f.write(text))

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)