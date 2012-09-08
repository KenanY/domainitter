#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* Domainitter - A Pastebin site auto-submitter
*
* Licensed under the MIT:
* http://www.opensource.org/licenses/mit-license.php
*
* Copyright (c) 2011–2012, Kenan Yildirim
"""

import argparse
import os.path
import random
import re
from httplib import HTTPConnection
from sys import exit


def split_thousands(s, sep=','):
    """ Borrowed from http://code.activestate.com/recipes/498181/#c4 """
    if len(s) <= 3:
        return s
    return split_thousands(s[:-3], sep) + sep + s[-3:]


def submit_site(query):
    """ Send a GET request to the update script """
    conn = HTTPConnection("www.pastebin.com")
    conn.request("GET", "/domain_update.php?q=%s&f=1" % query)
    conn.close()


def main():
    entry = None
    answer = None
    parser = argparse.ArgumentParser(
                                     description='''Updates domain records on
                                                    Pastebin''',
                                     epilog='''Copyright (c) 2011–2012,
                                               Kenan Yildirim''')
    parser.add_argument('scraps', type=int,
                        help='integer of how many domains you want to update',
                        nargs='?', default=1000000)
    parser.add_argument('-k', '--keyboard',
                        help='run the script without needing keyboard input.',
                        action='store_true', default=False)
    args = parser.parse_args()

    print 'Parsing website list...'
    if os.path.isfile('top-1m.txt'):
        with open('top-1m.txt') as f:
            entries = re.split("\n+", f)
    else:
        print 'Error: could not find website list!'
        exit()

    if args.keyboard:
        answer = '1'
    else:
        print '''Done!\n
        Time to make a choice:
        [1] Randomly select which websites to submit
        [2] Start from the most popular site, then work downwards'''
        answer = raw_input("> ")

    print '\n'

    if '1' in answer:
        print 'Randomly selecting sites!'
        print '=========='
        scraps = 1
        while scraps <= int(args.scraps):
            entryLine = re.split("[\W]?",
                                 entries[random.randint(1, 1000000)],
                                 1)
            submit_site(entryLine[1])
            print "[%s] %s (#%s)" % (split_thousands(str(scraps)),
                                     entryLine[1],
                                     split_thousands(entryLine[0]))
            scraps += 1
        exit()
    elif '2' in answer:
        print 'Starting from the top sites!'
        print '=========='
        for entry in entries:
            entryLine = re.split("[\W]?", entry, 1)
            if int(entryLine[0]) <= int(args.scraps):
                submit_site(entryLine[1])
                print "[%s] %s" % (str(split_thousands(entryLine[0])),
                                   entryLine[1])
            else:
                exit()
    else:
        print 'Learn to make choices!'


if __name__ == "__main__":
    exit(main())
