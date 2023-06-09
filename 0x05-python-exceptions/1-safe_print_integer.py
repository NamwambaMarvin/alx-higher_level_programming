#!/usr/bin/python3
def safe_print_integer(value):
    flag = True
    try:
        print("{:d}".format(value))
        return flag
    except (ValueError, TypeError):
        flag = False
        return flag
