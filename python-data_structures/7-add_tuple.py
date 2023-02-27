#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    while len(tuple_a) < 2 or len(tuple_b) < 2:
        a = list(tuple_a)
        b = list(tuple_b)
        a.append(0)
        b.append(0)
        tuple_a = tuple(a)
        tuple_b = tuple(b)
    new_tuple = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
    return new_tuple
