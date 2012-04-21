# domainitter

(formerly "Pastebin-Domains-Center-AutoSubmitter")

## WARNING:

Pastebin may **BAN YOUR IP ADDRESS** for using this script!

## About

So, for whatever reason, Pastebin has something called [Domains Center][2]. You can use it to quickly look up a comprehensive report on a domain. This is pretty neat, but when you come to an outdated report, you need to click something to update it. This is a simple Python script which uses the list of [top one million sites according to Alexa.com][1] and submits them to [Pastebin's domains center][2]. It parses through the list and sends GET requests to `www.pastebin.com/domain_update.php` in order to update the the archive of domains automatically.

## Usage

1. Clone [the repository][4] to get the files  
    `git clone git://github.com/KenanY/domainitter.git`
2. _Completely optional and virtually useless_: get an updated list of the top one million websites by downloading [Alexa.com's list][3] (~9.60 MB). You'll need to unzip the archive, then convert the list to a plaintext file (don't change its name, or you'll break stuff).
3. Run `domainitter.py`, optionally with an integer as an argument. It will be treated as the maximum number of domains you want to submit. Example: `domainitty.py 20` will only submit 20 domains  
4. Make a choice of whether you want the script to choose websites randomly to submit, or start from the top sites then work its way down  
5. ????  
6. PROFIT!!! (okay, not really)

   [1]: http://www.alexa.com/topsites (Top Sites)
   [2]: http://pastebin.com/domains (Pastebin - Domains Center)
   [3]: http://s3.amazonaws.com/alexa-static/top-1m.csv.zip (Download Alexa's list of top websites)
   [4]: https://github.com/KenanY/domainitter
