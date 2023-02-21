#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        return (a / b)
    except (NameError, ValueError):
        return ()
    finally:
        print("{:d}".format(int(a/b)))

# safe_print_division(8, 4)
