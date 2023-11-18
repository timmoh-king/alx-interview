#!/usr/bin/python3

"""
    Write a method that determines if a given data set
    represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
        Return: True if data is a valid UTF-8 encoding, else return False
        A character in UTF-8 can be 1 to 4 bytes long
        The data set can contain multiple characters
        The data will be represented by a list of integers
        Each integer represents 1 byte of data, therefore you only need
        to handle the 8 least significant bits of each integer
    """
    i = 0
    while i < len(data):
        num_bytes = 0
        byte = data[i]
        while byte & (128 >> num_bytes):
            num_bytes += 1
        if num_bytes == 0:
            i += 1
        elif num_bytes == 1 or num_bytes > 4:
            return False
        else:
            for j in range(1, num_bytes):
                if (i + j >= len(data) or
                        (data[i+j] & 0b11000000) != 0b10000000):
                    return False
            i += num_bytes
    return True
