# domainitter 
(formerly "Pastebin-Domains-Center-AutoSubmitter")

## WARNING ##
### Pastebin has banned my IP address because this script spams their servers! 
###I will no longer be working on it, and I highly recommend that you do not use it.

## About
This is a simple Python script which uses the list of [top one million sites according to Alexa.com][1] and submits them to [Pastebin's domains center][2]. I know the accuracy of Alexa's rankings are [not][4] [so][5] [good][6], but it doesn't matter for this script. All I needed was a large list of websites (and one million is quite enough).

I created this because I was bored one night.

## Usage

1. Fork [the repository][7] to get the files  
2. If you want, get an updated list of the top one million websites by downloading [Alexa.com's list][3]. You'll need to unzip the archive, then convert the list to a plaintext file (don't change its name, or you'll break stuff).
3. Run `domainitter.py`  
4. Make a choice of whether you want the script to choose websites randomly to submit, or start from the top sites then work its way down  
5. ????  
6. PROFIT!!! (okay, not really)

   [1]: http://www.alexa.com/topsites (Top Sites)
   [2]: http://pastebin.com/domains (Pastebin - Domains Center)
   [3]: http://s3.amazonaws.com/alexa-static/top-1m.csv.zip (Download Alexa's list of top websites)
   [4]: https://secure.wikimedia.org/wikipedia/en/wiki/Alexa_Internet#Accuracy_of_ranking_by_the_Alexa_Toolbar
   [5]: http://techcrunch.com/2007/08/13/alexa-says-youtube-is-now-bigger-than-google-theyre-wrong/
   [6]: http://techcrunch.com/2007/11/25/alexas-make-believe-internet/
   [7]: https://github.com/KenanY/domainitter
   