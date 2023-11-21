#!/usr/bin/env python3

"""
    Given a pile of coins of different values, determine the fewest number of
    coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
        Return: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
        coins is a list of the values of the coins in your possession
    """
    sum = 0

    if total <= 0:
        return 0

    for i in coins:
        sum += i

    if sum < total:
        return total - sum
    else:
        return -1
