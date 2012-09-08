# domainitter

(formerly "Pastebin-Domains-Center-AutoSubmitter")

[![Build Status](https://secure.travis-ci.org/KenanY/domainitter.png?branch=master)](http://travis-ci.org/KenanY/domainitter)

## WARNING:

Pastebin may **BAN YOUR IP ADDRESS** for using this script!

## About

So, for whatever reason, Pastebin has something called [Domains Center][2]. You can use it to quickly look up a comprehensive report on a domain. This is pretty neat, but when you come to an outdated report, you need to click something to update it. This is a simple Python script which uses the list of [top one million sites according to Alexa.com][1] and submits them to [Pastebin's domains center][2]. It parses through the list and sends GET requests to `www.pastebin.com/domain_update.php` in order to update the the archive of domains automatically.

## Usage

`domainitter.py` relies on `argparse` for parsing arguments. As such, you must use Python **2.7**. **This does not work with Python 3**... yet.

1. Clone [the repository][4] to get the files
    `git clone git://github.com/KenanY/domainitter.git`
2. _Completely optional and virtually useless_: get an updated list of the top one million websites by downloading [Alexa.com's list][3] (~9.60 MB). You'll need to unzip the archive, then convert the list to a plaintext file (don't change its name, or you'll break stuff).
3. Run `domainitter.py`, optionally with an integer as an argument. It will be treated as the maximum number of domains you want to submit. Example: `domainitty.py 20` will only submit 20 domains
4. Make a choice of whether you want the script to choose websites randomly to submit, or start from the top sites then work its way down
5. ????
6. PROFIT!!! <small>(not guaranteed)</small>

## Contributing

This is a really small project. You can easily hack on the `master` branch directly, so no need for complicated branches. Before you code a major change/feature (if there's such a thing possible for this script), open an issue in the [Issue Tracker][] so that we can discuss whether I'd be willing to accept such a change. This ensures that you don't go off wasting your time coding a feature I don't accept.

Also, please keep `domainitter.py` as [PEP 8][] compliant as possible. Use the [pep8 tool][] to check your code.

Tests are run on [Travis CI][]. Pretty much the only test is simply running the script itself, except with the argument `--keyboard` in order to skip the user input portion of the script. The current build status is displayed as a little image near the top of this README. You can check out all the builds [here][5].


   [1]: http://www.alexa.com/topsites
   [2]: http://pastebin.com/domains
   [3]: http://s3.amazonaws.com/alexa-static/top-1m.csv.zip
   [4]: https://github.com/KenanY/domainitter
   [5]: http://travis-ci.org/KenanY/domainitter
   [Issue Tracker]: https://github.com/KenanY/domainitter/issues
   [PEP 8]: http://www.python.org/dev/peps/pep-0008/
   [pep8 tool]: http://pypi.python.org/pypi/pep8
   [Travis CI]: http://travis-ci.org/
