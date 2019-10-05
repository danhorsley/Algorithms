#!/usr/bin/python

import sys

my_cache = {}
my_cache = {}
def making_change(n, d = [1,5,10,25,50],boost = 'y'):
  if n == 0:
    return 1
  else:
    if boost == 'y':
      booster = [n*500 for n in range(20)]
      for b in booster:
        making_change(b,[1,5,10,25,50],'n')
    label = 'e'.join([str(x) for x in d])
    for j in range(len(d)):
      l = 'e'.join([str(x) for x in d[j:]])
      if l not in my_cache.keys():
        my_cache[l] = {}
    k = 0
    for i in range(len(d)):
      temp_label = 'e'.join([str(x) for x in d[i:]])
      if n - d[i] == 0:
        k = k + 1
      elif n - d[i]>0:
        if n - d[i] in my_cache[temp_label].keys():
          kk = my_cache[temp_label][n-d[i]]
        else:
          kk = making_change(n - d[i], d[i:],'n')
        k = k + kk
      else:
        pass
    my_cache[label][n] = k
    return k

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")