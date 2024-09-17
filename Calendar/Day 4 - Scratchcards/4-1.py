# Advent of Code 2023
# Day 4-1: Scratchcards

import re


def parse_nums(s):
    nums = []

    for num in re.findall(r"\d+", s):
        nums.append(int(num))

    return nums


with open("input.txt") as file:
    total_score = 0

    for line in file:
        nums = line.split(":")[1].split("|")

        winning_nums = parse_nums(nums[0])
        all_nums = parse_nums(nums[1])

        score = 0

        for num in all_nums:
            if num in winning_nums:
                if score == 0:
                    score = 1
                else:
                    score *= 2

        total_score += score

    print(total_score)