#!/usr/bin/python3
"""
calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def factorization(n):
    """ prime factors of n or n if n is prime"""
    i = 2
    s = 0
    while i <= n:
        if n % i == 0:
            n = n // i
            s += i
            i -= 1
        i += 1
    return s


def minOperations(n):
    """
    fewest number of operations
    """
    if not isinstance(n, int) or n < 2:
        return 0
    return factorization(n)
