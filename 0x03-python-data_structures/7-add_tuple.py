#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a
    b = tuple_b
    if len(tuple_a) < 2:
        a += (0, 0)
    if len(tuple_b) < 2:
        b += (0, 0)
    return a[0] + b[0], a[1] + b[1]
