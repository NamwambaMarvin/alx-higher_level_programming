#!/usr/bin/python3
for j in range(10):
    for k in range(10):
        if j != k and j < k and j < 9:
            if j == 8 and k == 9:
                print("{}{}".format(j, k))
            else:
                print("{}{}, ".format(j, k), end='')
