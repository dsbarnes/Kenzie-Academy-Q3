#!/usr/bin/env python3
"""
Testing the imports of the modules I just made.
"""
from numseq.fib import fib
from numseq.geo import square, triangle, cube
from numseq.prime import is_prime, primes

__author__ = "Derek Barnes"


def main():
    # print(primes(7))
    for i in range(10):
        print('{}: {} {} {}'.format(i, square(i), triangle(i), cube(i)))


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
