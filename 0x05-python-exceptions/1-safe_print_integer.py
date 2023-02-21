#!/uar/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value), end='\n')
        return True
    except (NameError, TypeError):
        return False

# safe_print_integer(2)
