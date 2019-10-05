#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
my_cache = {}
cookie_options = [1,2,3]
def eating_cookies(n, cache=None):
  k = 0

  if n == 0:
    k = 1
  else:

    for co in cookie_options:
      if co<n:
        if n-co in my_cache.keys():
          k = k + my_cache[n-co]
        else:
          kk = eating_cookies(n-co,cache = my_cache)
          my_cache[n-co] = kk
          k = k + kk
      elif co==n:
        k = k+1
      else:
        pass

  return k

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')