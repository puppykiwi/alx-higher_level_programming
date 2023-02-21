#!/usr/bin/python3

def safe_print_division(a, b):
    div = (a / b)
    try:
        return (div)
    except (ZeroDivisionError):
        return (None)
    finally:
        print("Inside result: {:d}".format(div))

# safe_print_division(8, 0)
