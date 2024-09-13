def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except ValueError:
        return False
    return True
    

value = 89
has_been_printed = safe_print_integer(value)
if not has_been_printed:
    print("{} is not an integer".format(value))