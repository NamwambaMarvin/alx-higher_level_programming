#!/usr/bin/python3
def remove_char_at(str, n):
    newString = ""
    for index in range(len(str)):
        if index is not n:
            newString += str[index]
    return newString
