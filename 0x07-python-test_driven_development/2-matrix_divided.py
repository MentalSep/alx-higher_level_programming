#!/usr/bin/python3
""" This module divides all elements of a matrix """


def matrix_divided(matrix, div):
    """ This function divides all elements of a matrix """
    if isinstance(matrix, list) is False or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if isinstance(row, list) is False:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if isinstance(element, (int, float)) is False:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    return [[round(element / div, 2) for element in row] for row in matrix]
