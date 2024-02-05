#!/usr/bin/env python3


"""
Define functions to find the largest prime factor
of a number
"""


def largest_prime_factor(number):
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
    return number
