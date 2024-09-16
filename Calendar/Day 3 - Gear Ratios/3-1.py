# Advent of Code 2023
# Day 3-1: Gear Ratios

import re

with open("input.txt") as file:
    schematic = file.readlines()

    for y in range(len(schematic)):
        schematic[y] = schematic[y].strip()

    width = len(schematic[0])
    height = len(schematic)

    sum = 0

    for y in range(height):
        for num in re.finditer(r"\d+", schematic[y]):
            is_part_number = False

            start = num.start()
            end = num.end()

            for yy in range(y - 1, y + 2):
                for xx in range(start - 1, end + 1):
                    if yy == y and start <= xx < end:
                        continue

                    if xx < 0 or yy < 0:
                        continue

                    if xx >= width or yy >= height:
                        break

                    if schematic[yy][xx] != ".":
                        is_part_number = True

            if is_part_number:
                sum += int(num.group())

    print(sum)
