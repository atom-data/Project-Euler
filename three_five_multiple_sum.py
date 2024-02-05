#!/usr/bin/env python3

"""
Define function to sum multiples of 3 or 5
less than a given number
"""


def multiple_sum(num):
    multipleSum = 0
    for i in range(num):
        if (i % 3 == 0 or i % 5 == 0):
            multipleSum += i
    return multipleSum
