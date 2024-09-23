# Advent of Code 2023
# Day 14-1: Parabolic Reflector Dish

ROUND_ROCK = "O"
BLOCK_ROCK = "#"
EMPTY = "."


def parse_input(path):
    with open(path) as file:
        return [list(line.strip()) for line in file.readlines()]


def tilt(platform):
    for x in range(len(platform[0])):
        y = 0

        while y < len(platform):
            if y > 0 and platform[y][x] == ROUND_ROCK and platform[y - 1][x] == EMPTY:
                platform[y][x], platform[y - 1][x] = platform[y - 1][x], platform[y][x]
                y -= 1
            else:
                y += 1


def count_load(platform):
    sum = 0

    for y in range(len(platform)):
        sum += (len(platform) - y) * platform[y].count(ROUND_ROCK)

    return sum


platform = parse_input("input.txt")
tilt(platform)

print(count_load(platform))