# Advent of Code 2023
# Day 24-1: Never Tell Me The Odds

import re

AREA_MIN = 200000000000000
AREA_MAX = 400000000000000


class Path:
    def __init__(self, x, y, z, dx, dy, dz):
        self.x0, self.x1 = x, x + dx
        self.y0, self.y1 = y, y + dy
        self.z0, self.z1 = z, z + dz

    def find_future_intersection_x_y(self, other):
        am = (self.y1 - self.y0) / (self.x1 - self.x0)
        ac = self.y0 - am * self.x0

        bm = (other.y1 - other.y0) / (other.x1 - other.x0)
        bc = other.y0 - bm * other.x0

        if am == bm:
            return None, None

        x = (bc - ac) / (am - bm)
        y = am * x + ac

        is_future_a = (x - self.x0) * (self.x1 - self.x0) > 0
        is_future_b = (x - other.x0) * (other.x1 - other.x0) > 0

        if not (is_future_a and is_future_b):
            return None, None

        return x, y


def parse_input(path):
    paths = []

    with open(path) as file:
        for line in [row.strip() for row in file.readlines()]:
            nums = [int(num) for num in re.findall(r"-?\d+", line)]
            paths.append(Path(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5]))

    return paths


paths = parse_input("input.txt")
valid_intersection_count = 0

for i in range(len(paths)):
    for j in range(i):
        x, y = paths[i].find_future_intersection_x_y(paths[j])

        if x is None or y is None:
            continue

        if AREA_MIN <= x <= AREA_MAX and AREA_MIN <= y <= AREA_MAX:
            valid_intersection_count += 1

print(valid_intersection_count)