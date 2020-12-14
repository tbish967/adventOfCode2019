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
  flag = False
  min_start

  while not flag:
    for dep in departures:
      dep[]0
  
  #departures.sort(key=compare_ids, reverse=True)
  print(departures)
  # start time must = dep[0] * N - dep[1] for each dep in departures
  # where N is some interger, may be different for each

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
