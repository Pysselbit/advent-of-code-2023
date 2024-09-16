# Advent of Code 2023
# Day 3-2: Gear Ratios

import re


with open("input.txt") as file:
    schematic = file.readlines()

    for y in range(len(schematic)):
        schematic[y] = schematic[y].strip()

    width = len(schematic[0])
    height = len(schematic)

    sum = 0

    for y in range(height):
        for gear in re.finditer(r"\*", schematic[y]):
            ratios = []

            for yy in range(y - 1, y + 2):
                if yy < 0 or yy >= height:
                    continue

                for num in re.finditer(r"\d+", schematic[yy]):
                    if num.start() < gear.end() + 1 and num.end() > gear.start() - 1:
                        ratios.append(int(num.group()))

            if len(ratios) == 2:
                sum += ratios[0] * ratios[1]

    print(sum)