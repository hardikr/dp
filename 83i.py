#!/usr/bin/env python
# http://www.reddit.com/r/dailyprogrammer/comments/xdx4o/7302012_challenge_83_intermediate_indexed_file/

import sys
from optparse import OptionParser
import pprint
import string
import pickle

pp = pprint.PrettyPrinter(indent=2)

def main():
  parser = OptionParser()
  parser.add_option("-i", "--index",
                      action="store_true",
                      dest="index",
                      default=False,
                      help="Create index of files - supply with Comma separated list")
  parser.add_option("-s", "--search",
                      action="store_true",
                      dest="search",
                      default=False,
                      help="Search index with words - supply with Comma separated list")
  (options, args) = parser.parse_args()
  if(len(args) < 1):
    print "Supply -h parameter to get help"

  if(options.__dict__['index']):
    index(args[0].split(','))

  if(options.__dict__['search']):
    search(args[0].split(','))

def safeAddToDict(wordlist,word,f):
  try:
    wordlist[word].update([f])
  except KeyError as e:
    wordlist[word] = set([f])

def index(files):
  data = {}
  for fil in files:
    with open(fil) as f:
      data[fil] = f.read().translate(string.maketrans("",""), string.punctuation)

  wordlist = {}

  for f,d in data.items():
    for word in d.split():
      safeAddToDict(wordlist,word,f)

  pp.pprint(wordlist)
  srch = raw_input("Search for word: ")
  pickle.dump(wordlist, open('tests/83index.txt','wb'))
  print "Great, now you can search for words!"

def search(words):
  try:
    with open('tests/83index.txt') as f: pass
  except IOError as e:
   sys.exit('Please index with -i first. (use -h for help)')
  wordlist = pickle.load(open('tests/83index.txt','rb'))
  for word in words:
    if word in wordlist:
      print "-> "+word+" found in files: "
      for f in wordlist[word]:
        print f
    else:
      print word+" not found"

if __name__ == '__main__':
  main()