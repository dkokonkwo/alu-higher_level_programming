#!/usr/bin/python3
"""defines a function for matrix multiplication"""


def matrix_mul(m_a, m_b):
    """matrix multiplication"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for r in m_a:
        if type(r) is not list:
            raise TypeError("m_a must be a list of lists")
        if r == []:
            raise ValueError("m_a can't be empty")
        for n in r:
            if type(n) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for l in m_b:
        if type(l) is not list:
            raise TypeError("m_b must be a list of lists")
        if l == []:
            raise ValueError("m_b can't be empty")
        for n in l:
            if type(n) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    len_row_1 = []
    len_row_2 = []
    for row in m_a:
        len_row_1.append(len(row))
    if len(set(len_row_1)) > 1:
        raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        len_row_2.append(len(row))
    if len(set(len_row_2)) > 1:
        raise TypeError("each row of m_b must be of the same size")
    result = []
    for x in range(len(m_a)):
        result.append([])
    for y in result:
        for z in range(len(m_b)):
            y.append(0)
    for i in range(len(m_a)):
        # loop for columns
        for j in range(len(m_b)):
            # loop for multiplication
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
