#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" anagrams
    Command line interface that accepts a word file and returns a dictionary of
    anagrams for that file.

    Module provides a function find_anagrams which can be used to do the same
    for an arbitrary list of strings.

"""
__author__ = "Derek Barnes w/ assistance of Piero"

import sys
from collections import defaultdict


def alphabetize(string):
    """ alphabetize:
        Given a string, returns a string that
        includes the same letters in alphabetical order.
        Example:
        >>> print alphabetize('cab')
        abc
    """
    return "".join(sorted(string.lower()))


def find_anagrams(words):
    """ find_anagrams:
        Returns a dictionary with keys that are alphabetized words
        and values that are all words that, when alphabetized, match the key.
        Example:
        >>> print find_anagrams(['cat', 'dog', 'act'])
        {'dgo': ['dog'], 'act': ['cat', 'act']}
    """
    ana_dict = defaultdict(list)
    for word in words:
        # Super duper fast:
        ana_dict[alphabetize(word)].append(word)

        # Slow:
        # ana_list = [w for w in words if alphabetize(w) == alpha_word]

        # In the middle:
        # if alpha_word not in ana_dict:
        #     ana_dict[alpha_word] = [word]
        # else:
        #     ana_dict[alpha_word].append(word)

    return ana_dict


def main(filename):
    with open(filename, 'r') as f:
        word_list = f.read().split()
        print(word_list)


if __name__ == "__main__":
    main(sys.argv[1])
