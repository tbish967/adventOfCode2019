#!/usr/bin/env python3
import math

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return puzzle_input[:]

class Boat:
  def __init__(self):
    self.dir_dict = {
      'E': [1, 0],
      'S': [0, -1],
      'W': [-1, 0],
      'N': [0, 1]
    }
    self.pos_loop = [
      [1, 0],
      [0, -1],
      [-1, 0],
      [0, 1]
    ]
    self.current_dir = [1, 0]
    self.current_pos = [0, 0]

  def turn(self, direction, mag):
    turns = int(mag / 90)
    loop_ind = self.pos_loop.index(self.current_dir)
    if direction == 'R':
      self.current_dir = self.pos_loop[(loop_ind + turns) % len(self.pos_loop)]
    else:
      self.current_dir = self.pos_loop[loop_ind - turns % len(self.pos_loop)]
    
  def move(self, inst):
    direction = inst[0]
    mag = int(inst[1:])
    if direction in self.dir_dict:
      self.current_pos[0] += self.dir_dict[direction][0] * mag
      self.current_pos[1] += self.dir_dict[direction][1] * mag
    elif direction == 'F':
      self.current_pos[0] += self.current_dir[0] * mag
      self.current_pos[1] += self.current_dir[1] * mag
    else:
      self.turn(direction, mag)


class BoatWay:
  def __init__(self):
    self.current_pos = [0, 0]
    self.waypoint = [10, 1]
    self.dir_dict = {
      'E': [1, 0],
      'S': [0, -1],
      'W': [-1, 0],
      'N': [0, 1]
    }
  
  def rotate_way(self, direction, mag):
    turns = int(mag / 90) % 4
    if direction == 'L':
      turns = -turns + 4
    for i in range(turns):
      self.waypoint = [self.waypoint[1], -self.waypoint[0]]

  def execute(self, inst):
    direction = inst[0]
    mag = int(inst[1:])
    if direction in self.dir_dict:
      self.waypoint[0] += self.dir_dict[direction][0] * mag
      self.waypoint[1] += self.dir_dict[direction][1] * mag
    elif direction == 'F':
      self.current_pos[0] += self.waypoint[0] * mag
      self.current_pos[1] += self.waypoint[1] * mag
    else:
      self.rotate_way(direction, mag)

def part1():
  pi = parse_input()
  boat = Boat()

  for inst in pi:
    boat.move(inst)

  return abs(boat.current_pos[0]) + abs(boat.current_pos[1])

def part2():
  pi = parse_input()
  boat = BoatWay()

  for inst in pi:
    boat.execute(inst)

  return abs(boat.current_pos[0]) + abs(boat.current_pos[1])

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
