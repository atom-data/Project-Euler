#!/usr/bin/env python3

"""
Sum even Fibonacci numbers less than a
given limit
"""


def evenFibonacci(num):
    fibArray = [0, 1]
    i = 2
    while (fibArray[i-1] <= num):

        def fibonacci(n):
            if (n < len(fibArray)):
                return fibArray[n]
            else:
                fibArray.append(fibonacci(n-1) + fibonacci(n-2))
                return fibArray[n]
        fibonacci(i)
        i += 1
    evenSum = 0
    for i in fibArray:
        if (i % 2 == 0):
            evenSum += i
    return evenSum
