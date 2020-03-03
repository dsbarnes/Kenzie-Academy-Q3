#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a crete_dict function to avoid code duplication inside
print_words() and print_top().

"""
__author__ = "Derek Barnes /w help of Piero."
import sys
from collections import defaultdict


def create_dict(file_name):
    """"This function will create a dictionary of words and the associated counts."""

    count_dict = defaultdict(int)
    with open(file_name) as f:
        words = f.read().lower().split()

    for word in words:
        count_dict[word] += 1

    return count_dict


def print_words(file_name):
    """Will print a dictionary of words and the count
    of those words to the screen."""
    d = create_dict(file_name)

    for key in sorted(d.keys()):
        print(f"{key} : {d[key]}")


def print_top(file_name):
    """print the top 20 most frequent words."""
    d = create_dict(file_name)

    for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True)[:20]:
        print(f"{k} : {v}")


def main():
    """main()"""
    if len(sys.argv) != 3:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]

    if option == '--count':
        print_words(filename)

    elif option == '--topcount':
        print_top(filename)

    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
