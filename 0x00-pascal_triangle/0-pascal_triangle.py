#!/usr/bin/python3
"""
pascal's triangle
"""


def pascal_triangle(n):
    """function def pascal_triangle(n):
    that returns a list of integers representing
    the pascal traignle of n
    """

    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            c = 1
            for j in range(1, i + 1):
                level.append(c)
                c = c * (i - j) // j
            res.append(level)
    return res
