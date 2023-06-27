#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    index = 0;
    try:
        for element in my_list:
            if index < x:
                print("{}".format(element), end="")
                index += 1
        print()
    except KeyboardInterrupt:
        pass
    finally:
        return index
