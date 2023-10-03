#!/usr/bin/python3
""" This module contains a function that multiplies 2 matrices using NumPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ This function multiplies 2 matrices"""
    return np.matmul(m_a, m_b)
