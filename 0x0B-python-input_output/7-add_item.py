import sys

def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(str(my_obj).replace("'", '"'))

def load_from_json_file(filename):
    """Creates an object from a JSON file."""
    with open(filename, "r", encoding="utf-8") as file:
        return eval(file.read().replace('"', "'"))

if __name__ == "__main__":
    filename = "add_item.json"
    
    # Try to load the existing list from the file, or create an empty list if it doesn't exist.
    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    # Add all the command-line arguments to the list (excluding the script name).
    items.extend(sys.argv[1:])

    # Save the updated list back to the file.
    save_to_json_file(items, filename)
