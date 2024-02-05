#!/usr/bin/env python3
"""
Define function to get the sum of all numbers where
the sum of the all divisors and their quotient is a prime
"""


# Find all the primes less than or equal to the number
def prime_list(num):
    primes = [True for i in range(num + 1)]
    # boolean array
    p = 2
    while(p * p <= num):
        if (primes[p]):
            for i in range(p * p, num + 1, p):
                primes[i] = False
        p += 1
    return primes


def prime_sum(num):
    primes = prime_list(num + 1)
    # number 1 satistifies the property
    summation = 1
    for n in range(2, num+1, 2):
        i = 1
        while (i <= n/i):
            if (n % i == 0 and primes[i + n//i] is False):
                break
            else:
                i += 1
                if (n / i < i):
                    summation += n
    return summation


if __name__ == " __main__":
    from sys import argv

    num = argv[1]
    print(prime_sum(num))
