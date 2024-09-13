import sys
def safe_print_integer_err(value):
    try:
        print("{}".format(value))
        return True
    except (ValueError,TypeError) as e:
        print("Exception: {}".format(e),file=sys.stderr)
    return False
   
value = 89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))
