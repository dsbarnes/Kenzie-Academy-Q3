#!/usr/bin/env python3
"""
Web Scraper:
parses a URL passed in as a command line argument,
retrieve the text of the webpage at the specified URL
to find email addresses, URLs, and phone numbers included in the page.
"""

__author__ = "Derek Barnes"

import re
import sys
import argparse
import requests
from bs4 import BeautifulSoup


def parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("url", help="*Required* a URL")

    if len(sys.argv[1:]) == 0:
        parser.print_help()
        # parser.print_usage() # for just the usage line
        parser.exit()

    return parser.parse_args()


def request_url(url):
    req = requests.get(url)
    if req:
        # soup = BeautifulSoup(req.text, 'html.parser')
        # return soup
        return req.text
    return req.status_code


def soup(html):
    return BeautifulSoup(html, 'html.parser')


def get_tag(html, tag):
    matches = []
    for link in soup(html).find_all(tag):
        matches.append(link.get('href'))
    return matches


def find_emailesque_strings(html):
    pattern = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"

    return re.findall(pattern, html)


def find_urlesque_strings(html):
    pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

    return re.findall(pattern, html)


def find_phonesque_strings(html):
    pattern = r"1?\W*([2-9][0-8][0-9])\W*([2-9][0-9]{2})\W*([0-9]{4})(\se?x?t?(\d*))?"

    return re.findall(pattern, html)


def print_nicely(name, lst):
    print('\n' + name + '\n')
    for item in set(lst):
        if item is not None:
            print(item)


def main(args):
    """ Main entry point of the app """
    ns = parser()
    html_soup = request_url(ns.url)

    # There is probably a better place to define all this stuff.
    # Realistically it could just be a dictionary returned from a function...
    url_strings = find_urlesque_strings(html_soup)
    href_urls = get_tag(html_soup, 'a') + get_tag(html_soup, 'img')
    all_url_strings = url_strings + href_urls
    email_strings = find_emailesque_strings(html_soup)
    phone_strings = find_phonesque_strings(html_soup)

    
    print_nicely('URLS:', all_url_strings)
    print_nicely('EMAILS:', email_strings)
    # print_nicely('PHONE NUMBERS:', phone_strings)
    # That one little difference is all it took.
    print('\nPHONE NUMBERS:\n')
    for phone in set(phone_strings):
        if phone is not None:
            print(phone[0] + '-' + phone[1] + '-' + phone[2])


if __name__ == "__main__":
    """ This is executed when run from the command line """

    main(sys.argv[1:])
