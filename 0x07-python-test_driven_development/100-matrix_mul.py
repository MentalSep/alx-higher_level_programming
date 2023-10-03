#!/usr/bin/python3
""" This module contains a function that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """ This function multiplies 2 matrices"""
    if isinstance(m_a, list) is False:
        raise TypeError("m_a must be a list")
    if isinstance(m_b, list) is False:
        raise TypeError("m_b must be a list")

    for row in m_a:
        if isinstance(row, list) is False:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if isinstance(row, list) is False:
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for element in row:
            if isinstance(element, (int, float)) is False:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if isinstance(element, (int, float)) is False:
                raise TypeError("m_b should contain only integers or floats")

    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    newMatrix = [[0 for col in range(len(m_b[0]))] for row in range(len(m_a))]
    for row in range(len(m_a)):
        for col in range(len(m_b[0])):
            for i in range(len(m_b)):
                newMatrix[row][col] += m_a[row][i] * m_b[i][col]
    return newMatrix
