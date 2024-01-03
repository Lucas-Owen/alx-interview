#!/usr/bin/python3
"""This module defines a function pascal_triangle"""


def pascal_triangle(n):
    """This function returns pascal triangle upto level n"""
    result = []
    if n <= 0:
        return result
    prev = None
    j = 1
    for i in range(n):
        curr = []
        for k in range(j):
            if k == 0 or k == j - 1:
                curr.append(1)
            else:
                curr.append(prev[k-1] + prev[k])
        prev = curr
        result.append(curr)
        j += 1
    return result
