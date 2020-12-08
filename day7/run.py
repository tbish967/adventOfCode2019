#!/usr/bin/env python3
import re

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_bag(entry):
  words = entry.split(' ')
  phrases = [words[i:i + 4] for i in range(0, len(words), 4)]
  bag_color = words[0] + ' ' + words[1]
  refs = []
  if words[4] == 'no':
    return {bag_color: None}
  for phrase in phrases[1:]:
    refs.append([phrase[1] + ' ' + phrase[2], int(phrase[0])])
  return {bag_color: refs}

def recursive_find(c, d, bag):
  if not d[bag]:
    return False

  color_list = [k[0] for k in d[bag]]
  if c in color_list:
    return True
  else:
    for n in color_list:
      if recursive_find(c, d, n):
        return True
  return False

def search_dict(c, d):
  count = 0
  for bag in d:
    if recursive_find(c, d, bag):
      count += 1
  return count

def recursive_count(d, b):
  if not b:
    return 1
  count = 0
  print(b)
  for n in b:
    count += n[1] * recursive_count(d, d[n[0]])
  return count + 1

def count_nested(c, d):
  return recursive_count(d, d[c]) - 1

def parse_input():
  return puzzle_input[:]

def part1():
  pi = parse_input()
  bag_dict = {}
  
  for entry in pi:
    bag_dict.update(parse_bag(entry))

  return search_dict("shiny gold", bag_dict)
  #return bag_dict

def part2():
  pi = parse_input()
  bag_dict = {}

  for entry in pi:
    bag_dict.update(parse_bag(entry))

  return count_nested("shiny gold", bag_dict)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
