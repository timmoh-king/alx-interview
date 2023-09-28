#!/usr/bin/env python3

"""
    Create a function def pascal_triangle(n):
    that returns a list of integers representing the pascal's triangle of n:
    Return an empty list if n <= 0
    You can assume n will be an integer
"""


def pascal_triangle(n):
    """initialize an empty list"""
    triangle = []

    for i in range(n):
        """initialize each row with 1s"""
        row = [1] * (i + 1)

        """calculate values btn first and last element"""
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)

    return triangle
