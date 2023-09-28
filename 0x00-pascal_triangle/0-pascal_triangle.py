#!/usr/bin/python3

"""
    Create a function def pascal_triangle(n):
    that returns a list of integers representing the pascal's triangle of n:
    Return an empty list if n <= 0
    You can assume n will be an integer
"""


def pascal_triangle(n):
    """initialize an empty list"""
    empty_list = []

    if n > 0:
        for i in n:
            print(i)
    else:
        return []

