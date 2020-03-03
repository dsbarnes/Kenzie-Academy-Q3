#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "Derek Barnes! First solo submission!"

import cProfile
import StringIO
import pstats
import timeit
# import functools


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        r = func(*args, **kwargs)
        pr.disable()
        s = StringIO.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return r
    return inner


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


# def is_duplicate(title, movies):
#     """returns True if title is within movies list"""
#     for movie in movies:
#         if movie == title.lower():
#             return True
#     return False


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    movies.sort()
    duplicates = []

    for i, movie in enumerate(movies):
        if movie == movies[i - 1]:
            duplicates.append(movie)

    # while movies:
    #     movie = movies.pop()
    #     if is_duplicate(movie.lower(), movies):
    #         duplicates.append(movie)
    return duplicates


def timeit_helper(t):
    """Part A:  Obtain some profiling measurements using timeit"""
    num = 3
    # print('TIMEIT number=2:')
    # print(t.timeit(number=2))
    print('REPEAT repeat=7 number=3:')
    print(min(t.repeat(repeat=1, number=num)) / num)


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))

    t = timeit.Timer("main()", "print('setup')")
    timeit_helper(t)


if __name__ == '__main__':
    main()
