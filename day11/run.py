#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return puzzle_input[:]

def build_coordinates(rows):
  co_dict = {}
  for y in range(len(rows)):
    for x in range(len(rows[y])):
      co_dict[(x, y)] = rows[y][x]
  return co_dict

def count_neighbors(cod, c):
  count = 0
  for x in range(c[0]-1, c[0]+2):
    for y in range(c[1]-1, c[1]+2):
      if ((x, y) in cod) and (x, y) != c:
        if cod[(x, y)] == '#':
          count += 1
  return count

def count_neighbors_p2(cod, c):
  count = 0
  for x in range(-1, 2):
    for y in range(-1, 2):
      xx = x + c[0]
      yy = y + c[1]
      if [x, y] != [0, 0]:
        while ((xx, yy) in cod) and (cod[(xx, yy)] == '.'):
          xx += x
          yy += y
        if ((xx, yy) in cod) and (cod[(xx, yy)] == '#'):
          count += 1
  return count

def count_occupied(cod):
  return sum(cod[k] == '#' for k in cod)

def next_round(cod):
  new_cod = cod.copy()
  flag = False
  for c in cod:
    if cod[c] == 'L' and count_neighbors(cod, c) == 0:
      new_cod[c] = '#'
      flag = True
    elif cod[c] == '#' and count_neighbors(cod, c) > 3:
      new_cod[c] = 'L'
      flag = True
  return new_cod

def next_round_p2(cod):
  new_cod = cod.copy()
  flag = False
  for c in cod:
    if cod[c] == 'L' and count_neighbors_p2(cod, c) == 0:
      new_cod[c] = '#'
      flag = True
    elif cod[c] == '#' and count_neighbors_p2(cod, c) > 4:
      new_cod[c] = 'L'
      flag = True
  return new_cod

def display_dict(cod):
  current_y = 0
  string = ''
  for c in cod:
    if c[1] != current_y:
      current_y = c[1]
      string += '\n'
    string += cod[c]
  print(string)

def part1():
  pi = parse_input()
  cod = build_coordinates(pi)

  nr = next_round(cod)
  while nr != cod:
    cod = nr
    nr = next_round(cod)

  return count_occupied(nr)

def part2():
  pi = parse_input()
  cod = build_coordinates(pi)

  nr = next_round_p2(cod)
  while nr != cod:
    cod = nr
    nr = next_round_p2(cod)

  return count_occupied(nr)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
