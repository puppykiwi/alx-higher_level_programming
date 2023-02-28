#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print('{:d}'.format(int(my_list[i])), end='')
            count += 1
        except (TypeError, NameError, ValueError):
            continue
        except (IndexError):
            break

    print()
    return count

# safe_print_list_integers(my_list=[1,3,"shf",5], x=2)
