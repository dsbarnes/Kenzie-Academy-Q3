#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "Derek Barnes w/ assistance of Piero"

import sys
import argparse


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    # From: https://www.python-boilerplate.com/py2+executable+argparse

    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    parser.add_argument("text", help="text to be manipulated")

    parser.add_argument("-u", "--upper", help="convert text to uppercase",
                        action="store_true")
    parser.add_argument("-l", "--lower", help="convert text to lowercase",
                        action="store_true")
    parser.add_argument("-t", "--title", help="convert text to titlecase",
                        action="store_true")

    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args(args)
    result_text = ns.text

    if ns.upper:
        result_text = result_text.upper()

    if ns.lower:
        result_text = result_text.lower()

    if ns.title:
        result_text = result_text.title()

    return result_text


if __name__ == "__main__":
    print(main(sys.argv[1:]))
