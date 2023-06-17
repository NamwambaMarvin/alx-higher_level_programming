#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mul_mat = []

    if len(matrix) > 0:
        for one in matrix[:]:
            mul_mat.append(list(map(lambda x: x ** 2, one)))
    return mul_mat
