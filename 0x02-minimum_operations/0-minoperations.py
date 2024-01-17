#!/usr/bin/python3
"""This module defines the minOperations function"""


import math


def primes():
    """generate prime numbers"""
    i = 2
    while True:
        yield i
        j = i + 1
        while True:
            found = True
            for k in range(2, math.ceil(math.sqrt(j)) + 1):
                if j % k == 0:
                    found = False
                    break
            if found:
                i = j
                break
            j += 1

def minOperations(n):
    """Returns the minimum number of operations required to solve for n"""
    if n <= 1:
        return 0
    result = 0
    factors = primes()
    while n != 1:
        p = next(factors)
        while n % p == 0:
            result += p
            n /= p
    return result
