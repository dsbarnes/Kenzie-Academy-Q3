#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is supposed to check if the brackets in a string are properly matched.
"""
__author__ = "Your Github Username"
import sys


def count_brkts(line):
    opnB = ['(', '[', '{', '<', '(*']
    clsB = [')', ']', '}', '>', '*)']
    stack = []
    count = 0
    token = ''

    while line:
        token = line[0]
        if line.startswith('(*'):
            token = '(*'
        elif line.startswith('*)'):
            token = '*)'

        count += 1

        if token in opnB:
            stack.append(token)

        if token in clsB:
            matching_opener = opnB[clsB.index(token)]

            #!review this!!!
            if not stack or matching_opener != stack.pop():
                return count

        line = line[len(token):]

    if len(stack) > 0:
        return count

    return 0



def main(args):
    """Hello from main(): This function will check for properly nested brackets!"""

    with open('input.txt') as f:
        with open('output.txt', 'w') as f_out:
            for line in f:
                result = count_brkts(line)
                if result > 0:
                    f_out.write(f'No {result}\n')
                else:
                    f_out.write('Yes\n')


if __name__ == '__main__':
    main(sys.argv)
