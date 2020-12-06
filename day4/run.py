#!/usr/bin/env python3
import re


from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n\n')[:-1]

def format_passport_p1(x):
  return re.findall('(\S+):\S+', x)

def format_passport_p2(x):
  return re.findall('(\S+):(\S+)', x)

def validate_passport(passport, constraints):
  flag = True
  for field, function in constraints.items():
    if (field not in passport) or (not function(passport[field])):
      flag = False
  return flag

def ver_hgt(x):
  g = re.match('(\d+)(\w+)', x).groups()
  if g[1] == 'cm' and 150 <= int(g[0]) <= 193:
    return True
  elif g[1] == 'in' and 59 <= int(g[0]) <= 76:
    return True
  else:
    return False

def parse_input():
  return puzzle_input[:]

def part1():
  pi = parse_input()
  req_fields = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    'cid'
  }

  count = 0
  for passport in pi:
    s = set(format_passport_p1(passport))
    diff = req_fields - s
    if (not diff) or (diff == {'cid'}):
      count += 1

  return count

def part2():
  pi = parse_input()
  constraints = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': ver_hgt,
    'hcl': lambda x: bool(re.match('^#[\da-f]{6}$', x)),
    'ecl': lambda x: x in ['amb','blu','brn','gry','grn','hzl','oth'],
    'pid': lambda x: bool(re.match('^\d{9}$', x))
  }

  count = 0
  for passport in pi:
    p = dict(format_passport_p2(passport))
    if validate_passport(p, constraints):
      count += 1
  return count

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
