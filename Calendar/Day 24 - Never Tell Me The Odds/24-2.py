# Advent of Code 2023
# Day 24-2: Never Tell Me The Odds

import re
from z3 import *


class Path:
    def __init__(self, x, y, z, dx, dy, dz):
        self.x, self.y, self.z = x, y, z
        self.dx, self.dy, self.dz = dx, dy, dz


def parse_input(path):
    paths = []

    with open(path) as file:
        for line in [row.strip() for row in file.readlines()]:
            nums = [int(num) for num in re.findall(r"-?\d+", line)]
            paths.append(Path(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5]))

    return paths


paths = parse_input("input.txt")

x, y, z = Ints("x y z")
dx, dy, dz = Ints("dx dy dz")

s = Solver()

for i in range(3):
    path = paths[i]

    ti = Int(f"t{i}")
    s.add(ti >= 0)

    s.add(x + ti * dx == path.x + ti * path.dx)
    s.add(y + ti * dy == path.y + ti * path.dy)
    s.add(z + ti * dz == path.z + ti * path.dz)

s.check()
m = s.model()

x, y, z = m[x].as_long(), m[y].as_long(), m[z].as_long()

print(x + y + z)