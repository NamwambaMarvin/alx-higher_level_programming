#!/usr/bin/python3
for index in reversed(range(97, 123)):
    if (index % 2 == 0):
        print("{:c}".format(index), end='')
    else:
        print("{:c}".format(index - 32), end="")
