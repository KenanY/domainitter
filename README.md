# domainitter

Formerly "Pastebin-Domains-Center-AutoSubmitter"

This is a simple Python script which uses the list of [top one million sites according to Alexa.com][1] and submits them to [Pastebin's domains center][2].

I wrote this one night while I was bored. Guess that makes it a side project?

## Usage

1. Download, fork, or clone the repository
2. If you want, get an updated list of the top 1 million websites by downloading [Alexa.com's list][3]. You'll need to unzip the archive, then convert the list to a txt file (don't change its name, or you'll break stuff).
3. Run `domainitter.py`  
4. Make a choice of whether you want the script to choose websites randomly to submit, or start from the top sites then work its way down
5. ????
6. PROFIT!! (okay, not really)

   [1]: http://www.alexa.com/topsites (Top Sites)
   [2]: http://pastebin.com/domains (Pastebin - Domains Center)
   [3]: http://s3.amazonaws.com/alexa-static/top-1m.csv.zip (Download Alexa's list of top websites)