#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse

__author__ = "Derek Barnes"


def parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('dir', help='dest of "special files" to print')
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    args = parser.parse_args()
    return args


def get_special_fiels(directory):
    special_files = []
    for file_in_dir in os.listdir(directory):
        re_match_object = re.match(r"\w+__\w+__", file_in_dir)
        if re_match_object:
            special_files.append(file_in_dir)
    return special_files


def print_special_file_dirs(directory):
    special_files = get_special_fiels(directory)
    for special_file in special_files:
        print(os.path.abspath(special_file))

def copy_special_files(src, dest):
    special_files = get_special_fiels(src)

    if not os.path.exists(os.path.join(os.getcwd(), dest)):
        os.makedirs(dest)

    for f in special_files:
        full_src = os.path.join(src, f)
        full_dest = os.path.join(dest, f)
        shutil.copyfile(full_src, full_dest)


def zip_special_files(src, dest):
    special_files = get_special_fiels(src)
    command = ['zip', '-j', dest]
    command.extend(special_files)

    print('\nRunning the command {}'.format(' '.join(command)))
    subprocess.call(command)


def main():
    args = parser()
    # print(args)

    if not args.todir and not args.tozip:
        print_special_file_dirs(args.dir)
    if args.todir:
        copy_special_files(args.dir, args.todir)
    if args.tozip:
        zip_special_files(args.dir, args.tozip)


if __name__ == "__main__":
    main()
