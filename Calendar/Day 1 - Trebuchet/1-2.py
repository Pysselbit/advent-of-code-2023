# Advent of Code 2023
# Day 1-2: Trebuchet?!

import re

NUMS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open("input.txt") as file:
    sum = 0

    for line in file:
        a = b = None
        ai = bi = -1

        for num in NUMS:
            for match in re.finditer(num, line):
                n = NUMS.index(num) + 1
                i = match.start()

                if ai < 0 or i < ai:
                    a = n
                    ai = i

                if i > bi:
                    b = n
                    bi = i

        for i in range(len(line)):
            if not line[i].isdigit():
                continue

            n = int(line[i])

            if ai < 0 or i < ai:
                a = n
                ai = i

            if i > bi:
                b = n
                bi = i

        sum += int(a * 10 + b)

    print(sum)
