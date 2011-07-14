import random, re, os.path, time, httplib
from sys import exit

def splitthousands(s, sep=','):  
    if len(s) <= 3: return s  
    return splitthousands(s[:-3], sep) + sep + s[-3:]

def submitSite(query):
        conn = httplib.HTTPConnection("www.pastebin.com")
        conn.request("GET", "/domain_update.php?q=" + query + "&f=1")
        conn.close()

print '''Pastebin Domains Center AutoSubmitter
By KenanY
https://github.com/KenanY
\n
Parsing website list...'''
if os.path.isfile('top-1m.txt'):
        input = open("top-1m.txt").read()
        entries = re.split("\n+", input)
else:
        print '''###    Error!    ###
    Could not find website list!
    Make sure it is named "top-1m.txt" (without the quotes)
    If you don't have the list, download this file from Alexa:
        http://is.gd/AlexaList
    After that, unzip the file,
    open it in a text editor,
    and save it as a .txt file.
    Then try re-running this script.
    The script will automatically abort in 5 minutes,
    I'm sure you can read that fast.'''
        time.sleep(300)
        exit(0)
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
                submitSite(entryLine[1])
                print "[%s] %s (#%s)" % (splitthousands(str(scraps)), entryLine[1], splitthousands(entryLine[0]))
                scraps += 1
elif '2' in answer:
        print 'Starting from the top sites!'
        print '=========='
        for entry in entries:
                entryLine = re.split("[\W]?", entry, 1)
                submitSite(entryLine[1])
                print "[%s] %s" % (str(splitthousands(entryLine[0])), entryLine[1])
else:
        print 'Learn to make choices!'
        exit(0)
