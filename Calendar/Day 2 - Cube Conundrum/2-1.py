# Advent of Code 2023
# Day 2-1: Cube Conundrum

import re

R = "red"
G = "green"
B = "blue"

RN = 12
GN = 13
BN = 14


def get_color(set, color):
    match = re.search(rf"\d+ {color}", set)

    if match:
        return int(re.findall(r"\d+", match.group())[0])

    return 0


with open("input.txt") as file:
    sum = 0

    for line in file:
        is_possible = True

        for set in line.split(";"):
            r = get_color(set, R)
            g = get_color(set, G)
            b = get_color(set, B)

            if r > RN or g > GN or b > BN:
                is_possible = False
                break

        if is_possible:
            sum += int(re.findall(r"\d+", line)[0])

    print(sum)
