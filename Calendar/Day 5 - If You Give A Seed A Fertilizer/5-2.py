# Advent of Code 2023
# Day 5-2: If You Give A Seed A Fertilizer

import re


class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Map:
    def __init__(self, source, destination, length):
        self.start = source
        self.end = source + length
        self.shift = destination - source

    def apply(self, unmapped, mapped):
        index = 0
        while index < len(unmapped):
            range = unmapped[index]
            if range.start >= self.end or range.end <= self.start:
                index += 1
                continue

            unmapped.remove(range)
            if range.start < self.start:
                unmapped.append(Range(range.start, self.start))
                range.start = self.start
            if range.end > self.end:
                unmapped.append(Range(self.end, range.end))
                range.end = self.end

            mapped.append(Range(range.start + self.shift, range.end + self.shift))


def parse_seed_ranges(input):
    ranges = []

    nums = re.findall(r"\d+", input)
    for i in range(0, len(nums), 2):
        start = int(nums[i])
        end = start + int(nums[i + 1])
        ranges.append(Range(start, end))

    return ranges


def parse_maps(input, index):
    maps = []

    nums = re.findall(r"\d+", input[index])
    while len(nums) == 3:
        maps.append(Map(int(nums[1]), int(nums[0]), int(nums[2])))

        index += 1
        if index == len(input):
            break

        nums = re.findall(r"\d+", input[index])

    return maps


with open("input.txt") as file:
    lines = file.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    seed_ranges = parse_seed_ranges(lines[0])
    map_sets = []
    for i in range(1, len(lines)):
        if "map" in lines[i]:
            map_sets.append(parse_maps(lines, i + 1))

    mapped = seed_ranges
    for map_set in map_sets:
        unmapped = mapped
        mapped = []

        for map in map_set:
            map.apply(unmapped, mapped)

        for range in unmapped:
            mapped.append(range)

    closest = -1
    for range in mapped:
        if closest < 0 or range.start < closest:
            closest = range.start

    print(closest)