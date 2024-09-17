# Advent of Code 2023
# Day 5-1: If You Give A Seed A Fertilizer

import re


class Map:
    def __init__(self, sources, destinations, ranges):
        self.sources = sources
        self.destinations = destinations
        self.ranges = ranges

    def get_destination(self, source):
        for i in range(len(self.sources)):
            if self.sources[i] <= source < self.sources[i] + self.ranges[i]:
                return source + self.destinations[i] - self.sources[i]

        return source


def parse_seeds(input):
    nums = []

    for num in re.findall(r"\d+", input):
        nums.append(int(num))

    return nums


def parse_map(input, index):
    sources = []
    destinations = []
    ranges = []

    nums = re.findall(r"\d+", input[index])

    while len(nums) == 3:
        sources.append(int(nums[1]))
        destinations.append(int(nums[0]))
        ranges.append(int(nums[2]))

        index += 1
        if index == len(input):
            break

        nums = re.findall(r"\d+", input[index])

    return Map(sources, destinations, ranges)


with open("input.txt") as file:
    lines = file.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    seeds = parse_seeds(lines[0])
    maps = []
    for i in range(1, len(lines)):
        if "map" in lines[i]:
            maps.append(parse_map(lines, i + 1))

    min = -1
    for seed in seeds:
        for map in maps:
            seed = map.get_destination(seed)

        if min < 0 or seed < min:
            min = seed

    print(min)