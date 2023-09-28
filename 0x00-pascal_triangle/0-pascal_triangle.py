#!/usr/bin/python3

"""
    Create a function def pascal_triangle(n):
    that returns a list of integers representing the pascal's triangle of n:
    Return an empty list if n <= 0
    You can assume n will be an integer
"""


def pascal_triangle(n):
    """initialize an empty list"""
    triangle = [[1]]

    for i in range(n - 1):
        temp = [0] + triangle[-1] + [0]
        row = []
        for j in range(len(triangle[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        triangle.append(row)
    return triangle
