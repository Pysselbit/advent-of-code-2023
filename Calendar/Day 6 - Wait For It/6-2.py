# Advent of Code 2023
# Day 6-2: Wait For It

import math
import re


with open("input.txt") as file:
    lines = file.readlines()

    t0 = int(re.search(r"\d+", lines[0].replace(" ", "")).group())
    d0 = int(re.search(r"\d+", lines[1].replace(" ", "")).group())

    # Effin' PQ-formeln:
    # v * t > d0
    # v * (t0 - v) - d0 > 0
    # v * v - t0 * v + d0 < 0
    # p = -t0, q = d0
    v1 = -(-t0 / 2) + math.sqrt(pow(-t0 / 2, 2) - d0);
    v2 = -(-t0 / 2) - math.sqrt(pow(-t0 / 2, 2) - d0);

    v1 = math.floor(v1)
    v2 = math.ceil(v2)

    print(abs(v2 - v1) + 1)