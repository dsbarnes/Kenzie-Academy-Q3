#!/usr/local/bin python3

"""
Program to watch for changes in a directory.
If a file is added or removed, a message will be logged.
"""

__author__ = "Derek Barnes with assistance of Piero"

import os
import sys
import time
import argparse
import logging
import signal


exit_flag = False
logger = logging.getLogger(__name__)
logging.basicConfig(
    format='%(asctime)s.%(msecs)03d %(name)-12s %(levelname)-8s [%(threadName)-12s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S', filename="dirwatch.log", level=logging.DEBUG)


# This is PYTHON3 not 2 -- program will error out if you run in py2
if sys.version_info.major < 3:
    raise RuntimeError("Must be run in python3")


def search_for_magic(filename, start_line, magic):
    with open(filename) as f:
        line_num = 0
        for line_num, line in enumerate(f):
            if line_num < start_line:
                continue
            if magic in line:
                logger.debug(
                    f"Found magic text (on line {line_num}) : {magic}")
    return line_num + 1


def dirwatch(dw, magicstring, interval=1, extension=''):
    """
    Places a directory under scrutienty
    """
    watchpath = os.path.abspath(dw)
    watchfiles = {}

    while not exit_flag:
        # Add files into dictionary:
        for f in os.listdir(watchpath):
            if f not in watchfiles and f.endswith(extension):
                logger.debug(f"Now watching {f}")
                watchfiles[f] = 0

        # Remove files from dictionary, no longer in path:
        for f in list(watchfiles):
            if f not in os.listdir(watchpath):
                watchfiles.pop(f)
                logger.debug(f"Removed file {f}")

        for f, startline in watchfiles.items():
            last_line = search_for_magic(os.path.join(
                watchpath, f), startline, magicstring)
            watchfiles[f] = last_line

        time.sleep(float(interval))


def create_parser():
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required arguments
    parser.add_argument("dir", help="The directory to watch for changes")
    parser.add_argument("magicstring", help="The string to search for")

    # Optional arguments
    parser.add_argument("-e", "--extension",
                        help="Watch a specific file extension", default="")
    parser.add_argument("-i", "--interval", default=1,
                        help="Set the refresh interval in sec (defaults to 1)")

    if len(sys.argv[1:]) == 0:
        parser.print_help()
        parser.exit()

    return parser.parse_args()


def main(args):
    """ Main entry point of the app """
    ns = args
    dirwatch(ns.dir, ns.magicstring, ns.interval, ns.extension)


if __name__ == "__main__":

    args = create_parser()
    main(args)

