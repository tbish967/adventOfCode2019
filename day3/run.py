#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

class Route:
  def __init__(self, right, down):
    self.treeCount = 0
    self.right = right
    self.down = down

def parse_input():
  return puzzle_input[:]

def test_tree(r, yPos, pattern):
  xPos = int((yPos * r.right) / r.down)
  if xPos >= len(pattern):
    xPos %= len(pattern)
  if (pattern[xPos] == '#') and (yPos % r.down == 0):
    return True
  else:
    return False

def part1():
  pi = parse_input()
  r = Route(3,1)
  for yPos,pattern in enumerate(pi):
    if test_tree(r, yPos, pattern):
      r.treeCount += 1
  return r.treeCount

def part2():
  pi = parse_input()
  route_directions = [[1,1],[3,1],[5,1],[7,1],[1,2]]
  routes = []

  for direction in route_directions:
    routes.append(Route(direction[0], direction[1]))

  for yPos,pattern in enumerate(pi):
    for r in routes:
      if test_tree(r, yPos, pattern):
        r.treeCount += 1

  multiplier = 1
  for r in routes:
    multiplier *= r.treeCount
  return multiplier

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
