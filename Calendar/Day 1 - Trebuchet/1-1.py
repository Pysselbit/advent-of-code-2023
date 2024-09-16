# Advent of Code 2023
# Day 1-1: Trebuchet?!

with open("input.txt") as file:
    sum = 0

    for line in file:
        a = b = None

        for char in line:
            if char.isdigit():
                if a is None:
                    a = char
                b = char

        sum += int(a + b)

    print(sum)