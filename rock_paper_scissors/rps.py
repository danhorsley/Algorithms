#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  if n == 0:
    new_combos = [[]]
  elif n>1:
    rps = ['rock','paper','scissors']
    new_combos = [(combo+[choice]) for combo in rock_paper_scissors(n-1)for choice in rps ]
  else:
    new_combos = [['rock'],['paper'],['scissors']]

  return new_combos


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')