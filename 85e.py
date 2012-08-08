#!/usr/bin/env python
# http://www.reddit.com/r/dailyprogrammer/comments/xq0yv/832012_challenge_85_easy_rowcolumn_sorting/

import sys

with open("tests/85e.txt") as f:
  data = f.read()

arr= [[int(n) for n in row.split(' ')] for row in data.split('\n')]

rs = [(sum(row),row) for row in arr] # rowsums
cs = [(sum(col),col) for col in zip(*arr)] # colsums

# To forgo formatting: print [row[1] for row in sorted(rs)]
for row in sorted(rs):
  for el in row[1]:
    sys.stdout.write(str(el)+' ')
  print "" #newline

print "------------------------- "

# To forgo formatting: print zip(*[col[1] for col in sorted(cs)])
for row in zip(*[col[1] for col in sorted(cs)]):
  print " ".join(map(str,row))


  # for el in zip(*col[1]):
  #   sys.stdout.write(str(el)+' ')
  # print "" #newline