#!/usr/bin/env python3
import re

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return puzzle_input[:]

def format_entry(entry):
  p = re.compile('(^\d+)-(\d+) (\w): (\w+$)')
  return p.match(entry).groups()

def validate_pass_ct(min, max, letter, pwd):
  if min <= pwd.count(letter) <= max:   
    return True
  else:
    return False

def validate_pass_pos(first, last, letter, pwd):
  if (pwd[first-1] == letter) ^ (pwd[last-1] == letter):
    return True
  else:
    return False

def part1():
  pi = parse_input()
  count = 0
  for entry in pi:
    fEntry = format_entry(entry)
    if validate_pass_ct(int(fEntry[0]), int(fEntry[1]), fEntry[2], fEntry[3]):
      count += 1
  return count

def part2():
  pi = parse_input()
  count = 0
  for entry in pi:
    fEntry = format_entry(entry)
    if validate_pass_pos(int(fEntry[0]), int(fEntry[1]), fEntry[2], fEntry[3]):
      count += 1
  return count

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
