#!/usr/bin/env python3
import re
import itertools

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  pi = puzzle_input[:]
  masks = []
  current_mask = None

  for line in pi:
    line = line.split(' ')
    if line[0] == 'mask':
      if current_mask:
        masks.append([current_mask, current_entry])
      current_mask = line[2]
      current_entry = []
    else:
      mem = re.match('mem\[(\d+)\]', line[0]).groups(0)[0]
      val = line[2]
      current_entry.append([mem, val])
  masks.append([current_mask, current_entry])
  return masks

def part1():
  pi = parse_input()
  mem = {}
  
  for group in pi:
    mask = group[0]
    ones = 0
    zeros = 0
    for i in range(len(mask)):
      i_comp = -i + 35
      if mask[i] == 'X':
        ones += 2 ** i_comp
      else:
        ones += int(mask[i]) * (2 ** i_comp)
        zeros += int(mask[i]) * (2 ** i_comp)
    
    for ml in group[1]:
      index = int(ml[0])
      val = int(ml[1])
      mem[index] = (zeros | val) & ones

  vsum = 0
  for entry in mem:
    vsum += mem[entry]

  return vsum

def part2():
  pi = parse_input()
  mem = {}
  
  for group in pi:
    mask = group[0]
    floats = []
    zeros = 0 # zero for all bits not set by mask
    null_ones = 0 # one for all non-mask bits, zero for mask
    dc_list = []

    for i in range(len(mask)):
      i_comp = -i + 35
      if mask[i] == 'X':
        floats += [2 ** i_comp]
      else:
        zeros += int(mask[i]) * (2 ** i_comp)
        null_ones += 2 ** i_comp
    
    for i in range(len(floats)+1):
      for combo in itertools.combinations(floats, i):
        dc_list += [sum(combo)]

    for ml in group[1]:
      # Set non-null ones
      index = int(ml[0]) | zeros
      # Set mask bits to zero
      index = index & null_ones
      val = int(ml[1])
      for dc in dc_list:
        mem[index + dc] = val
    
  vsum = 0
  for entry in mem:
    vsum += mem[entry]

  print(len(dc_list))
  return vsum

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
