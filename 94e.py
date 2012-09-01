#!/usr/bin/env python
# http://www.reddit.com/r/dailyprogrammer/comments/z6o4k/9012012_challenge_94_easy_elemental_symbols_in/

import sys

if len(sys.argv) != 2:
    sys.exit('Usage: %s word-to-breaking-bad' % sys.argv[0])

with open('tests/94ept.csv') as f:
	pt = f.read()

pt = pt.split(',')
word = sys.argv[1].lower()

for el in pt:
	if el.lower() in word:
		print word.replace(el.lower(),'['+el+']')