import random, re, urllib2, os.path, time
from sys import exit

def submitSite(query):
        opener.open("http://pastebin.com/domain_update.php?q=" + query + "&f=1")
        opener.close()

print 'Pastebin Domains Center AutoSubmitter'
print 'By KenanY'
print 'https://github.com/KenanY'
print '\n'
print 'Parsing website list...'
if os.path.isfile('top-1m.txt'):
        input = open("top-1m.txt").read()
        entries = re.split("\n+", input)
else:
        print '''###    Error!    ###
    Could not find website list!
    Make sure it is named "top-1m.txt" (without the quotes)
    If you don't have the list, download this file from Alexa:
        http://is.gd/AlexaList
            ( actual URL: http://s3.amazonaws.com/alexa-static/top-1m.csv.zip )
    After that, unzip the file,
    open it in a text editor,
    and save it as a .txt file.
    Then try re-running this script.
    The script will automatically abort in 5 minutes,
    I'm sure you can read that fast.'''
        time.sleep(300)
        exit(0)
print 'Creating website opener...'
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0')]
print 'Done!'
print '\n'
print 'Time to make a choice: '
print '[1] Randomly select which websites to submit'
print '[2] Start from the most popular site, then work downwards'
print '\n'
answer = raw_input("> ")
if '1' in answer:
        print 'Randomly selecting sites!'
        print '=========='
        scraps = 1
        while scraps < 1000000:
                entryLine = re.split("[\W]?", entries[random.randint(1,1000000)], 1)
                submitSite(entryLine[1])
                print "[%s] %s (#%s)" % (str(scraps), entryLine[1], entryLine[0])
                scraps += 1
elif '2' in answer:
        print 'Starting from the top sites!'
        print '=========='
        for entry in entries:
                entryLine = re.split("[\W]?", entry, 1)
                submitSite(entryLine[1])
                print "[%s] %s" % (str(entryLine[0]), entryLine[1])
else:
        print 'Learn to make choices!'
        exit(0)
