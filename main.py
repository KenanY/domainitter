import re
import urllib2
import sys 
import random

input = open("top-1m.txt").read()
entries = re.split("\n+", input)

print 'Pastebin Domains Center AutoSubmitter'
print 'By KenanY'
print 'https://github.com/KenanY'
print '=========='
print 'Time to make a choice: '
print '[1] Randomly select which websites to submit'
print '[2] Start from the most popular site, then work downwards'
answer = raw_input("> ")
if '1' in answer:
        print 'Randomly selecting sites!'
        print '=========='
        scraps = 1
        while scraps < 1000000:
                entryLine = re.split("[\W]?", entries[random.randint(1,1000000)], 1)
                opener = urllib2.build_opener()
                opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1')]
                opener.open("http://pastebin.com/domain_update.php?q=" + entryLine[1] + "&f=1")
                opener.close()
                print "[%s] %s (#%s)" % (str(scraps), entryLine[1], entryLine[0])
                scraps += 1
elif '2' in answer:
        print 'Starting from the top sites!'
        print '=========='
        scraps = 1
        for entry in entries:
                entryLine = re.split("[\W]?", entry, 1)
                opener = urllib2.build_opener()
                opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1')]
                opener.open("http://pastebin.com/domain_update.php?q=" + entryLine[1] + "&f=1")
                opener.close()
                print "[%s] %s" % (str(scraps), entryLine[1])
                scraps += 1
