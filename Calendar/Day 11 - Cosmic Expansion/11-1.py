# Advent of Code 2023
# Day 11-1: Cosmic Expansion

GALAXY = "#"
EMPTY = "."


class Galaxy:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def expand_empty_space(space):
    empty_rows = [True] * len(space)
    empty_columns = [True] * len(space[0])

    for y in range(len(space)):
        for x in range(len(space[y])):
            if space[y][x] != EMPTY:
                empty_rows[y] = empty_columns[x] = False

    for y in range(len(empty_rows) - 1, -1, -1):
        if empty_rows[y]:
            space.insert(y, [EMPTY] * len(space[0]))

    for x in range(len(empty_columns) - 1, -1, -1):
        if empty_columns[x]:
            for y in range(len(space)):
                space[y].insert(x, EMPTY)


def find_galaxies(space):
    galaxies = []

    for y in range(len(space)):
        for x in range(len(space[y])):
            if space[y][x] == GALAXY:
                galaxies.append(Galaxy(x, y))

    return galaxies


def sum_distances(galaxies):
    distances = [[]]

    for i in range(len(galaxies)):
        distances.append([])
        a = galaxies[i]

        for j in range(i):
            b = galaxies[j]
            distances[i].append(abs(b.x - a.x) + abs(b.y - a.y))

    return sum([sum(x) for x in distances])


with open("input.txt") as file:
    space = [list(x.strip()) for x in file.readlines()]
    expand_empty_space(space)

    galaxies = find_galaxies(space)
    sum = sum_distances(galaxies)

    print(sum)