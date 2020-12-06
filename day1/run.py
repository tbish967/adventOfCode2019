#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return puzzle_input[:]

def part1():
  pi = parse_input()
  for e, i in enumerate(pi):
    for j in pi[e:]:
      i = int(i)
      j = int(j)
      if (i + j == 2020):
        return(i * j)

def part2():
  pi = parse_input()
  for e, i in enumerate(pi):
    for f, j in enumerate(pi[e:]):
      for k in pi[f:]:
        i = int(i)
        j = int(j)
        k = int(k)
        if (i + j + k == 2020):
          return(i * j * k)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
