#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        return (a / b)
    except (NameError, ValueError,ZeroDivisionError):
        return ("None")
    finally:
        print("{:d} / {:d} = {:d}".format(a,b,int(a/b)))

# safe_print_division(8, 0)
