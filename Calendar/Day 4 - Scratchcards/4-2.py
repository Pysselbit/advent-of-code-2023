# Advent of Code 2023
# Day 4-2: Scratchcards

import re


class Scratchcard:
    def __init__(self, winning_nums, all_nums):
        self.count = 1
        self.winning_nums = winning_nums
        self.all_nums = all_nums


def parse_nums(s):
    nums = []

    for num in re.findall(r"\d+", s):
        nums.append(int(num))

    return nums


with open("input.txt") as file:
    cards = []
    for line in file:
        nums = line.split(":")[1].split("|")
        cards.append(Scratchcard(parse_nums(nums[0]), parse_nums(nums[1])))

    total_card_count = 0
    for i in range(len(cards)):
        card = cards[i]
        total_card_count += card.count

        score = 0
        for num in card.all_nums:
            if num in card.winning_nums:
                score += 1

        for j in range(score):
            cards[i + 1 + j].count += card.count

    print(total_card_count)
