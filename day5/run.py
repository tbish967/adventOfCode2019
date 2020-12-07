#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def decode_bin(m, l):
  bin_list = [m[k] for k in l]
  return sum(c << i for i, c in enumerate(bin_list[::-1]))

def find_row(boarding_pass):
  bin_map = {'B': 1, 'F': 0}
  return decode_bin(bin_map, boarding_pass[:-3])

def find_column(boarding_pass):
  bin_map = {'L': 0, 'R': 1}
  return decode_bin(bin_map, boarding_pass[-3:])

def find_missing(min_id, max_id, id_set):
  return (set(range(min_id, max_id)) - id_set).pop()

def parse_input():
  return puzzle_input[:]

def part1():
  pi = parse_input()
  max_id = 0
  for boarding_pass in pi:
    current_id = 8 * find_row(boarding_pass) + find_column(boarding_pass)
    max_id = max(current_id, max_id)
  return max_id

def part2():
  pi = parse_input()
  id_set = set()
  min_id = 128
  max_id = 0

  for boarding_pass in pi:
    pass_id = find_row(boarding_pass) * 8 + find_column(boarding_pass)
    id_set.add(pass_id)
    min_id = min(min_id, pass_id)
    max_id = max(max_id, pass_id)
  return find_missing(min_id, max_id, id_set)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
