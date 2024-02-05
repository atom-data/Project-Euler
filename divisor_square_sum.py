#!/usr/bin/env python3

"""
Define function to find the sum of squares of divisors
that are perfect squares
"""


# Find the sum of squares of divisors
def divisor_square_sum(n):
    summation = 0
    i = 1
    while (i <= n/i):
        if (n % i == 0):
            summation += i**2 + (n//i)**2
        i += 1
    return summation


def perfect_square_sum(num):
    perfectSum = 0
    for i in range(2, num+1):
        squareSum = divisor_square_sum(i)
        k = i
        while (k <= squareSum/k):
            if (k == squareSum/k):
                perfectSum += squareSum
            k += 1
    return perfectSum
