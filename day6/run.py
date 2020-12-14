#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n\n')

def get_answers_p1(group):
  dist_ans = set()
  for form in group.split('\n'):
    dist_ans.update(set(form))
  return dist_ans

def get_answers_p2(group):
  first_iter = True
  for form in group.split('\n'):
    if first_iter:
      dist_ans = set(form)
      first_iter = False
    else:
      dist_ans.intersection_update(set(form))
  return dist_ans

def parse_input():
  return puzzle_input[:]

def part1():
  pi = parse_input()
  count = 0
  for group in pi:
    count += len(get_answers_p1(group))
  return count

def part2():
  pi = parse_input()
  count = 0
  for group in pi:
    count += len(get_answers_p2(group))
  return count

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
