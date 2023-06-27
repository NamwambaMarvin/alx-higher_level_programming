#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    total = 0
    for index in range(x):
        try:
            if type(my_list[index]) is int and total < x:
                print("{:d}".format(my_list[index]), end='')
                total += 1
        except (TypeError, ValueError):
            continue
    print()
    return total
