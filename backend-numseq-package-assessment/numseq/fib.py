#!/usr/bin/env python3
"""
Computes the Nth Fibonacci Number.
"""

__author__ = "Derek Barnes"


def fib(n):
    """ Returns the nth Fibonacci number """
    start_sequence = [0, 1]

    if n == 0 or n == 1:
        return start_sequence[n]
    while n > 1:
        last_number = start_sequence[-1]
        second_to_last_number = start_sequence[-2]
        start_sequence.append(last_number + second_to_last_number)
        n -= 1
    return start_sequence[-1]
