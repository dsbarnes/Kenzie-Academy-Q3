#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a directory path, search all files in the path for a given text string
within the 'word/document.xml' section of a MSWord .dotm file.
"""
__author__ = "Derek Barnes"
import os
import sys
import argparse
import zipfile

# print(args.dir)
# print(args.text)


def main(args):
    # This will be the default path if none is provided:
    path_to_dotm_files = os.path.join(os.getcwd(), 'dotm_files')

    # Set up argparse arguments:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--dir', help='Specify the directory to search for .dotm files',
        default=path_to_dotm_files)
    parser.add_argument(
        'text', help='The text to string search .dotm filse for')

    # .parse_args() 'activates' our command line arguments
    args = parser.parse_args()

    # This is the list of files we will need to search through
    # as well as some counters that we will need for proper output
    file_list = os.listdir(args.dir)
    file_list = [f for f in file_list if f.endswith('.dotm')]
    searches = 0
    matches = 0

    # This is the 'business logic'
    # For each file in the dir, open it as a zip file
    for file_name in file_list:
        full_path = os.path.join(args.dir, file_name)
        with zipfile.ZipFile(full_path) as z:
            # namelist will show the contents of the zipped file
            names = z.namelist()

            # Now that we have a zip file open,
            # We need to add to the number of searches
            searches += 1

            # Open the zip file:
            with z.open('word/document.xml') as doc:
                # Read the lines:
                for line in doc:
                    # If the position that we find the provided --text
                    # is >= 0, we found a match (cause -1 is no match)
                    text_position = line.find(args.text)
                    if text_position >= 0:

                        # We found a match:
                        matches += 1

                        print("Match found in file {}".format(file_name))
                        print("... {} ...".format(line[text_position-40: text_position+41]))

    print("Files searched: {}".format(searches))
    print("Files matched: {}".format(matches))


if __name__ == '__main__':
    main(sys.argv[1:])
