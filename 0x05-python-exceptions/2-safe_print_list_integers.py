#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    total = 0
    for element in my_list:
        try:
            if type(element) is int:
                print("{:d}".format(element), end='')
                total += 1
        except TypeError:
            continue
    print()
    return total
