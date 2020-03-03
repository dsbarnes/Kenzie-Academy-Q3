#!/usr/bin/env python3
"""
Logpuzzle exercise

Copyright 2010 Google Inc.
Licensed under the Apache License, Version 2.0
http://www.apache.org/licenses/LICENSE-2.0

"""
__author__ = "Derek Barnes w/ Help of Piero"

import os
import re
import sys
import urllib.request
import argparse


def read_urls(filename):
    """
    Reads an apache log file nd searches for a URL pattern.
    If the pattern exists in the provided file,
    and the word 'puzzle' is contained in the matched pattern,
    a list of matches will be created, and returned.

    Otherwise, it returns an empty list.
    """
    url_list = []
    regx = r'GET\s(\S+)'

    with open(filename) as logfile:
        for line in logfile:
            re_obj = re.search(regx, line)
            if re_obj:  # a match was found
                url = re_obj.group(1)
                if 'puzzle' in url:
                    url_list.append(url)
    return url_list


def sort_url_list(url_list):
    """
    Takes in a list of urls returned from read_urls
    and sorts according to a pre determined alphabeticle pattern.
    """
    def sort_key(s):
        re_obj = re.search(r'([a-z]+)-([a-z]+)\.', s)
        if re_obj:
            # first_key = re_obj.group(1)
            key = re_obj.group(2)

        return key

    url_list = sorted(set(url_list), key=sort_key)
    return url_list


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on..
    Creates the directory if necessary.
    """
    try:
        os.mkdir(dest_dir)
    except FileExistsError:
        pass  # if you can't make the directory, fine, continue

    # Make a counter, and name all the images we just downloaded
    # We want to do this here b/c we are concerned about what goes into
    # the file, as well as the order that it is placed in the file.
    i = 0
    for img in img_urls:
        name_for_img = 'img' + str(i)
        i += 1
        path = os.path.join(dest_dir, name_for_img)
        urllib.request.urlretrieve('http://code.google.com/' + img, path)


def create_index_html(dest_dir):
    """
    Creates an index.html file in a destination directory.
    The document will contain a series of img tags.
    The src attributes of the img tags will be the names of the files.
    """
    new_index = os.path.join(os.getcwd(), dest_dir, 'index.html')
    number_of_files = len(os.listdir(dest_dir))
    htmlopen = '<!DOCTYPE html>\n<html lang="en">\n<body>\n'
    htmlclose = '</body>\n</html>\n'

    with open(new_index, 'a+') as index:
        index.write(htmlopen)

        # For each file in the dir,
        # Files will need to be named img{N}
        # That is done in the download img function
        for i in range(number_of_files):
            index.write(f'<img src=img{i}>')

        index.write(htmlclose)


def create_parser():
    """Create an argument parser object"""
    parser = argparse.ArgumentParser(
        description='Parser to get HTTP paths from an Apache log file')
    parser.add_argument(
        'logfile', help='apache logfile to extract urls from')
    parser.add_argument(
        '-d', '--todir',  help='destination directory for downloaded images')
    if len(sys.argv) == 1:
        parser.print_help()
        parser.exit()
    return parser.parse_args()


def main(args):
    """Main driver for the log-puzzle-assessment"""
    parser = create_parser()
    if not args:
        parser.print_usage()
        sys.exit(1)

    # Drive it home!
    img_urls = sort_url_list(read_urls(parser.logfile))
    dest_dir = os.path.join(os.getcwd(), parser.todir)
    download_images(img_urls, dest_dir)
    create_index_html(dest_dir)


if __name__ == '__main__':
    main(sys.argv[1:])
