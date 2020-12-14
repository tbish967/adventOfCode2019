#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def validate_entry(n, s):
  for i in s:
    if (n - i) in s:
      return True
  return False

def parse_input():
  return puzzle_input[:]

def part1():
  pi = [int(k) for k in parse_input()]
  code_lst = pi[:25]
  code_set = set(code_lst)

  for code in pi[25:]:
    if not validate_entry(code, code_set):
      return code
    code_set.remove(code_lst[0])
    code_lst.pop(0)
    code_set.add(code)
    code_lst.append(code)
  
  return False

def part2():
  pi = [int(k) for k in parse_input()]
  target = part1()
  window = pi[:2]
  pi_index = 2
  running_sum = sum(window)
  while running_sum != target:
    if running_sum < target:
      window.append(pi[pi_index])
      running_sum += window[-1]
      pi_index += 1
    elif running_sum > target:
      running_sum -= window.pop(0)
      
  return min(window) + max(window)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
