# Advent of Code 2023
# Day 12-1: Hot Springs

import re

OPERATIONAL = "."
DAMAGED = "#"
UNKNOWN = "?"


class SpringSet:
    def __init__(self, springs, groups):
        self.springs = springs
        self.groups = groups


def parse_input(path):
    with open(path) as file:
        spring_sets = []

        for line in [x.strip().split() for x in file.readlines()]:
            springs = line[0]
            groups = tuple(int(x) for x in re.findall(r"\d+", line[1]))
            spring_sets.append(SpringSet(springs, groups))

        return spring_sets


def get_valid_permutations(springs, groups):
    if springs == "":
        return 1 if len(groups) == 0 else 0

    if len(groups) == 0:
        return 1 if DAMAGED not in springs else 0

    sum_valid_permutations = 0

    if springs[0] in ".?":
        sum_valid_permutations += get_valid_permutations(springs[1:], groups)

    if springs[0] in "#?":
        if (groups[0] <= len(springs) and OPERATIONAL not in springs[:groups[0]] and
                (len(springs) == groups[0] or springs[groups[0]] != DAMAGED)):
            sum_valid_permutations += get_valid_permutations(springs[groups[0] + 1:], groups[1:])

    return sum_valid_permutations


spring_sets = parse_input("input.txt")
sum_valid_permutations = sum([get_valid_permutations(x.springs, x.groups) for x in spring_sets])

print(sum_valid_permutations)