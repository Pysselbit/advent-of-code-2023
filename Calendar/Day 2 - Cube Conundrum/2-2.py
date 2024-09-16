# Advent of Code 2023
# Day 2-2: Cube Conundrum

import re

R = "red"
G = "green"
B = "blue"


def get_color(set, color):
    match = re.search(rf"\d+ {color}", set)

    if match:
        return int(re.findall(r"\d+", match.group())[0])

    return 0


with open("input.txt") as file:
    sum = 0

    for line in file:
        r = g = b = 0

        for set in line.split(";"):
            r = max(r, get_color(set, R))
            g = max(g, get_color(set, G))
            b = max(b, get_color(set, B))

        sum += r * g * b

    print(sum)
