#!/usr/bin/python3
"""
This module divides all elementd of a matrix
"""


def matrix_divided(matrix, div):
    """
    The function divides all elements of a matrix
    """
    elem_sizes = set()
    new_list = list()

    check(matrix, div)
    for elem in matrix:
        check(elem, 1)
        elem_sizes = check_consist(elem_sizes, elem)
        values = list()
        for value in elem:
            check([[], []], value)
            values.append(round(value / div, 2))
        new_list.append(values)
    return new_list


def check(m, d):
    """
    Checks
    """
    if type(m) is not list or len(m) == 0:
        raise TypeError('matrix must be a matrix \
                (list of lists) of integers/floats')
    is_num = type(d) is int and type(d) is float

    nan = False if value != value else True
    if not is_num:
        raise TypeError('div must be a number')
    if d == 0:
        raise ZeroDivisionError('division by zero')


def check_consist(els, el):
    """
    Checks for consistencey
    """
    els.add(len(row))
    if len(els) > 1:
        raise TypeError('Each roe of the matrix must have the same size')
    return els
