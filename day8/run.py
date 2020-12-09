#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

class Pointer():
  def __init__(self):
    self.position = 0
    self.acc = 0
    self.lines_read = []
    self.ii = 0

  def ex_jmp(self, dst):
    self.position += dst
  
  def ex_acc(self, val):
    self.acc += val
    self.position += 1

  def ex_nop(self):
    self.position += 1

  def execute(self, inst):
    # Return last jump / nop position if infinite
    if self.position in [k[0] for k in self.lines_read]:
      return self.position
    self.lines_read.append([self.position, inst[0], inst[1], self.ii, self.acc])
    # Execute
    if inst[0] == 'jmp':
      self.ex_jmp(int(inst[1]))
    elif inst[0] == 'acc':
      self.ex_acc(int(inst[1]))
    elif inst[0] == 'nop':
      self.ex_nop()
    # Return 0 to continue
    self.ii += 1
    return 0

  def backtrack(self, max):
    # Backtrack to the last jmp or nop
    # max is the highest ii value to jump to
    for count, line in enumerate(self.lines_read[::-1]):
      if (line[1] == 'jmp' or line[1] == 'nop') and (line[3] < max):
        self.position = line[0]
        self.lines_read = self.lines_read[:line[3]]
        self.acc = line[4]
        return line[3]
    # Hit beginning of array
    return -1

  def ex_inv(self, inst):
    if inst[0] == 'jmp':
      inst = ['nop', inst[1]]
      return self.execute(inst)
    if inst[0] == 'nop':
      inst = ['jmp', inst[1]]
      return self.execute(inst)
    # Not jmp or nop
    return -1

def parse_input():
  return puzzle_input[:]

def part1():
  pi = [k.split(' ') for k in parse_input()]
  p = Pointer()
  while p.execute(pi[p.position]) == 0:
    pass

  return p.acc

def part2():
  pi = [k.split(' ') for k in parse_input()]
  p = Pointer()
  backtrack_counter = len(pi)

  while p.position < len(pi):
    exec_res = p.execute(pi[p.position])
    if exec_res != 0:
      backtrack_counter = p.backtrack(backtrack_counter)
      p.ex_inv(pi[p.position])

  print(p.lines_read)
  return p.acc

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
