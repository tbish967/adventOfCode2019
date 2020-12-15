#!/usr/bin/env python3
import numpy as np

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return puzzle_input[:]

def get_departures(seq):
  return [int(k) for k in seq.split(',') if k != 'x']

def get_deps_keys(seq):
  return [[int(k), e] for e, k in enumerate(seq.split(',')) if k != 'x']

def compare_ids(e):
  return e[0]

def part1():
  pi = parse_input()
  ref_time = int(pi[0])

  departures = get_departures(pi[1])
  deltas = [int(np.ceil(ref_time / dep)) * dep - ref_time for dep in departures]
  
  min_ind = np.argmin(deltas)
  return departures[min_ind] * deltas[min_ind]

def part2():
  pi = parse_input()
  ref_time = int(pi[0])
  departures = get_deps_keys(pi[1])
  multiplier = 1
  time = 0

  print(departures)
  for i in range(len(departures)-1):
    bus_id = departures[i+1][0]
    offset = departures[i+1][1]
    multiplier *= departures[i][0]

    while (time + offset) % bus_id != 0:
      time += multiplier
  
  return time

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
