#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return puzzle_input[0].split(',')

def part1():
  pi = parse_input()
  turn_dict = {}
  last_turn = None

  for i in range(1, len(pi) + 1):
    turn_dict[int(pi[i-1])] = i
    last_turn = int(pi[i-1])

  for i in range(len(pi) + 1, 20):
    if last_turn in turn_dict:
      last_turn = i - turn_dict[last_turn]
      print(i)
      print(last_turn)
      print(turn_dict)
      turn_dict[last_turn] = i
    else:
      turn_dict[0] = i
      last_turn = 0

  return turn_dict

def part2():
  pi = parse_input()

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
