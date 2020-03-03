#!/usr/bin/env python3
"""
Module for listing and checking prime numbers.
"""

__author__ = "Derek Barnes"


def is_prime(n):
    """ Returns a boolean indicating whether N is a prime number """
    if n <= 0:
        raise ValueError("N must be greater than 0")

    if n == 1 or n == 2:
        return True

    for factor in range(2, n):
        if n % factor == 0:
            return False
    return True


def primes(n):
    """ Returns a list of prime numbes up to but not including N """
    prime_list = [number for number in range(1, n) if is_prime(number)]
    return prime_list


# This actually isn't at all necessary for the assignment, but its cool as hell
def gen_primes():
    # Sieve of Eratosthenes
    # Code by David Eppstein, UC Irvine, 28 Feb 2002
    # http://code.activestate.com/recipes/117119/
    """ Creates a generator that will produce prime numbers to inf """

    # Maps composites to primes witnessing their compositeness.
    D = {}
    q = 2  # The running integer that's checked for primeness
    while True:
        if q not in D:  # q is a new prime.
            yield q  # Yield it and mark its first multiple that isn't
            D[q * q] = [q]  # already marked in previous iterations
        else:  # q is composite.
            # D[q] is the list of primes that divide it.
            # Since we've reached q, we no longer need it in the map,

            # but we'll mark the next multiples of its witnesses
            # to prepare for larger numbers
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1
