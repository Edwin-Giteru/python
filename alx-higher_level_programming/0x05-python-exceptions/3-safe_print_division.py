def safe_print_division(a, b):

    try:
       result = a / b
    except ZeroDivisionError:
        return  None
    finally:
        print("Inside_result:{}".format(result))

    return result

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))