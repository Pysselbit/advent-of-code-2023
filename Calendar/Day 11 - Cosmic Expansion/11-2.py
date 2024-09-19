# Advent of Code 2023
# Day 11-2: Cosmic Expansion

EXPANSION = 1000000

GALAXY = "#"
EMPTY = "."

ROWS = "rows"
COLUMNS = "columns"


class Galaxy:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def find_empty_space(space):
    empty_rows = [True] * len(space)
    empty_columns = [True] * len(space[0])

    for y in range(len(space)):
        for x in range(len(space[y])):
            if space[y][x] != EMPTY:
                empty_rows[y] = empty_columns[x] = False

    return {ROWS: empty_rows, COLUMNS: empty_columns}


def find_galaxies(space):
    galaxies = []

    for y in range(len(space)):
        for x in range(len(space[y])):
            if space[y][x] == GALAXY:
                galaxies.append(Galaxy(x, y))

    return galaxies


def sum_distances(galaxies, empty_space):
    distances = [[]]

    for i in range(len(galaxies)):
        distances.append([])
        a = galaxies[i]

        for j in range(i):
            distance = 0
            b = galaxies[j]

            for x in range(min(a.x, b.x), max(a.x, b.x)):
                distance += EXPANSION if empty_space[COLUMNS][x] else 1
            for y in range(min(a.y, b.y), max(a.y, b.y)):
                distance += EXPANSION if empty_space[ROWS][y] else 1

            distances[i].append(distance)

    return sum([sum(x) for x in distances])


with open("input.txt") as file:
    space = [list(x.strip()) for x in file.readlines()]
    empty_space = find_empty_space(space)

    galaxies = find_galaxies(space)
    sum = sum_distances(galaxies, empty_space)

    print(sum)