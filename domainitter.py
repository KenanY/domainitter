"""
* Domainitter - A Pastebin site auto-submitter
*
* Licensed under the MIT:
* http://www.opensource.org/licenses/mit-license.php
*
* Copyright (c) 2011, Kenan Yildirim
"""

import httplib
import os.path
import random
import re
import time
from sys import exit

def split_thousands(s, sep=','):     # Borrowed from http://code.activestate.com/recipes/498181/#c4
    if len(s) <= 3: return s  
    return split_thousands(s[:-3], sep) + sep + s[-3:]

def submit_site(query):
    conn = httplib.HTTPConnection("www.pastebin.com")
    conn.request("GET", "/domain_update.php?q=" + query + "&f=1")
    conn.close()

print '''#####   domainitter   #####
By KenanY
https://github.com/KenanY
\n
Parsing website list...'''

if os.path.isfile('top-1m.txt'):
    input = open("top-1m.txt").read()
    entries = re.split("\n+", input)
else:
    print '''###    Error!    ###
    Could not find website list!'''
    while True:
        pass
    
print '''Done!
\n
Time to make a choice: 
[1] Randomly select which websites to submit
[2] Start from the most popular site, then work downwards'''
answer = raw_input("> ")
print '\n'

if '1' in answer:
    print 'Randomly selecting sites!'
    print '=========='
    scraps = 1
    while scraps < 1000000:
        entryLine = re.split("[\W]?", entries[random.randint(1,1000000)], 1)
        submit_site(entryLine[1])
        print "[%s] %s (#%s)" % (split_thousands(str(scraps)), entryLine[1], split_thousands(entryLine[0]))
        scraps += 1
elif '2' in answer:
    print 'Starting from the top sites!'
    print '=========='
    for entry in entries:
        entryLine = re.split("[\W]?", entry, 1)
        submit_site(entryLine[1])
        print "[%s] %s" % (str(split_thousands(entryLine[0])), entryLine[1])
else:
    print 'Learn to make choices!'
    exit(0)
