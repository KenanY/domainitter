#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* Domainitter — A Pastebin Domains center auto-updater
*
* Licensed under the MIT:
* http://www.opensource.org/licenses/mit-license.php
*
* Copyright (c) 2011–2014, Kenan Yildirim
*
*
*
* ArgsList parsing
* ================
*
* Copyright (c) 2012, Kenneth Reitz
* All rights reserved.
*
* Redistribution and use in source and binary forms, with or without
* modification, are permitted provided that the following conditions are met:
*
* Redistributions of source code must retain the above copyright notice, this
* list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice,
* this list of conditions and the following disclaimer in the documentation
* and/or other materials provided with the distribution.
* THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
* AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
* IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
* ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
* LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
* CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
* SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
* INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
* CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
* ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
* POSSIBILITY OF SUCH DAMAGE.
"""

import os
import random
import re
import sys
import urllib
from sys import exit
from sys import argv
from collections import OrderedDict


if sys.version_info[0] == 3:
    string_type = str
else:
    string_type = basestring


def _is_collection(obj):
    """Tests if an object is a collection. Strings don't count."""

    if isinstance(obj, string_type):
        return False

    return hasattr(obj, '__getitem__')


class ArgsList(object):
    """CLI Argument management."""

    def __init__(self, args=None, no_argv=False):
        if not args:
            if not no_argv:
                self._args = argv[1:]
            else:
                self._args = []
        else:
            self._args = args

    def __getitem__(self, i):
        try:
            return self.all[i]
        except IndexError:
            return None

    @property
    def grouped(self):
        """Extracts --flag groups from argument list.
           Returns {format: Args, ...}
        """

        collection = OrderedDict(_=ArgsList(no_argv=True))
        _current_group = None

        for arg in self.all:
            if arg.startswith('-'):
                _current_group = arg
                collection.setdefault(arg, ArgsList(no_argv=True))
            else:
                if _current_group:
                    collection[_current_group]._args.append(arg)
                else:
                    collection['_']._args.append(arg)

        return collection

    @property
    def all(self):
        """Returns all arguments."""

        return self._args


def split_thousands(s, sep=','):
    """ Borrowed from http://code.activestate.com/recipes/498181/#c4 """
    if len(s) <= 3:
        return s
    return split_thousands(s[:-3], sep) + sep + s[-3:]


def submit_site(query):
    """ Send a GET request to the update script """
    params = urllib.urlencode({'q': query, 'f': 1})
    urllib.urlopen('http://pastebin.com/domain_update.php' + '?' + params)


def main():
    args = ArgsList()
    gr = args.grouped
    answer = '1'

    print 'Parsing website list...'
    if os.path.isfile('top-1m.txt'):
        with open('top-1m.txt') as f:
            entries = re.split("\n+", f.read())
    else:
        print 'Error: could not find website list!'
        exit()

    print 'Parsing arguments...'
    if '-n' in gr:
        maxScraps = gr['-n'][:1][0]
        print 'Found custom limit: ' + maxScraps
    else:
        maxScraps = 1000000

    if '-c' in gr:
        answer = str(gr['-c'][:1][0])

    print 'Done parsing stuff.'

    if answer is '1':
        print 'Random'
        print '======'
        scraps = 1
        while scraps <= int(maxScraps):
            entryLine = re.split("[\W]?",
                                 entries[random.randint(1, 1000000)],
                                 1)
            submit_site(entryLine[1])
            print "[%s] %s (#%s)" % (split_thousands(str(scraps)),
                                     entryLine[1],
                                     split_thousands(entryLine[0]))
            scraps += 1
        exit()
    elif answer is '2':
        print 'Ordered'
        print '======='
        for entry in entries:
            entryLine = re.split("[\W]?", entry, 1)
            if int(entryLine[0]) <= int(maxScraps):
                submit_site(entryLine[1])
                print "[%s] %s" % (str(split_thousands(entryLine[0])),
                                   entryLine[1])
            else:
                exit()
    else:
        print 'Learn to make choices!'


if __name__ == "__main__":
    exit(main())
