#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return [int(k) for k in puzzle_input[:]]

def list_combine(min_index, max_number, x):
  for e, i in enumerate(x, min_index):
    if e < len(x) - 1:
      print(i)
      s = i + x[e+1]
      if s <= max_number:
        x[e] = s
        x.pop(e+1)
        return x
  return False

def get_diffs(sequence):
  diffs = []
  for i in range(1,len(sequence)):
    diffs.append(sequence[i] - sequence[i-1])
  return diffs

def get_streaks(diffs, num):
  streak = 0
  streaks = []
  for i in range(len(diffs)):
    if diffs[i] == num:
      streak += 1
    elif streak != 0:
      streaks.append(streak)
      streak = 0
  return streaks

def build_tl(num):
  tl = [1, 2, 4]
  for n in range(len(tl), num):
    tl.append(tl[n-3] + tl[n-2] + tl[n-1])
  return tl

def part1():
  pi = parse_input() + [0]
  pi.sort()
  pi.append(pi[-1] + 3)
  jd_1 = 0
  jd_3 = 0
  for i in range(0, len(pi)-1):
    diff = pi[i+1] - pi[i]
    if diff == 1:
      jd_1 += 1
    elif diff == 3:
      jd_3 += 1

  return jd_1 * jd_3

def part2():
  pi = parse_input() + [0]
  pi.sort()
  pi.append(pi[-1] + 3)

  diffs = get_diffs(pi)
  streaks = get_streaks(diffs[:], 1)

  tl = build_tl(max(streaks))

  count = 1
  for streak in streaks:
    count *= tl[streak-1]
  return count

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
