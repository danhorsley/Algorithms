#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):

  def my_reader(file, format = 'f'):
    #this function reads teh text file then sorts it by value per cost unit (vpcu)
    #or if files has already been turned into list it just return a list with vpcu added
    if format == 'f':
      f=open(file, "r")
      lines = f.readlines()
      d = []
      for l in lines:
          d.append(l.rstrip().split())
      #my_dict = {}
      my_list = []
      for entry in d:
          entry = [int(x) for x in entry] + [int(entry[2])/int(entry[1])]
          my_list.append(entry)
          #my_dict[entry[0]] = {'cost':entry[1],'value':entry[2],'ratio':entry[2]/entry[1]}
      my_list.sort(key = lambda x :x[3],reverse=True)
      return my_list
    #this is to read the format in teh tester
    else:
      my_list = []
      for entry in file:
        entry = [int(x) for x in entry] + [int(entry[2])/int(entry[1])]
        my_list.append(entry)
      my_list.sort(key = lambda x :x[3],reverse=True)
      return my_list


  my_cache = {}
  def maxer(items,bs=100):
      #cache check.  make label first of string of IDs
      label = 'e'.join([str(x[0]) for x in items])
      try:
          max_score = my_cache[label][bs]
      except:
          #strip items down to ONLY items which have cost less than bag size
          items = [x for x in items if x[1]<=bs]

          #return null score if that leaves you with no items
          if len(items)==0:#bs < min([x[1] for x in items]):
              return [0,[],0]
          else:
              #max_score in form [score, [components],weight]
              max_score = [0,[],0]
              for i in range(len(items)-1):
                      # set score equal to value of first item in list + max score for remainder
                      remainder = maxer(items[i+1:],bs-items[i][1])
                      #these are progress checks in case loops is taking a while
                      #print('i',items[i])
                      #print('r',remainder)
                      temp_max = [items[i][2] + remainder[0], [items[i][0]] + remainder[1],items[i][1]+remainder[2]]
                      if temp_max[0] > max_score[0] and temp_max[2]<=bs:
                          max_score = temp_max
                          #print(max_score)
              last_item_score = items[-1][2]
              if last_item_score > max_score[0]:
                  max_score = [last_item_score, [items[-1][0]], items[-1][1]]

              #labeling and cacheing the maxscore

              if label not in my_cache.keys():
                  my_cache[label]={}
              my_cache[label][bs] = max_score
          
      return max_score

  all_items = my_reader(items, format = 'l')[:45]
  answer = maxer(all_items,capacity)
  answer[1].sort()
  return {'Value': answer[0], 'Chosen': answer[1]}

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')