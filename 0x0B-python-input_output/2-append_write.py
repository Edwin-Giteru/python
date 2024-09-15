def append_write(filename="",text=""):
    with open(filename,"a",encoding="utf-8") as f:
        print(f.write(text))

nb_characters_added = append_write("my_first_file.txt", "This School is so cool!\n")
print(nb_characters_added)
