#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as v:
        sys.stderr.write("Exception " + str(v) + "\n")
        return False
    except TypeError as v:
        sys.stderr.write("Exception " + str(v) + "\n")
        return False
