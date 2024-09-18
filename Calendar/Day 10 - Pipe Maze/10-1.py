# Advent of Code 2023
# Day 10-1: Pipe Maze

class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y


NORTH = Vec(0, -1)
EAST = Vec(1, 0)
SOUTH = Vec(0, 1)
WEST = Vec(-1, 0)

DIRECTIONS = [NORTH, EAST, SOUTH, WEST]


def has_exit(grid, x, y, dx, dy):
    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
        return False

    pipe = grid[y][x]

    if dx == 0 and dy == -1:
        return pipe in "|LJ"
    if dx == 1 and dy == 0:
        return pipe in "-LF"
    if dx == 0 and dy == 1:
        return pipe in "|7F"
    if dx == -1 and dy == 0:
        return pipe in "-J7"

    return False


with open("input.txt") as file:
    grid = [x.strip() for x in file.readlines()]

    # Find start:
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "S":
                start = Vec(x, y)
                pos = Vec(x, y)

    # Find starting direction:
    for direction in DIRECTIONS:
        if has_exit(grid, pos.x + direction.x, pos.y + direction.y, -direction.x, -direction.y):
            next = direction
            break

    pos.x += next.x
    pos.y += next.y
    distance = 1

    # Find loop:
    while grid[pos.y][pos.x] != "S":
        for direction in DIRECTIONS:
            if direction.x == -next.x and direction.y == 0 or direction.y == -next.y and direction.x == 0:
                continue

            if has_exit(grid, pos.x, pos.y, direction.x, direction.y):
                next = direction
                break

        pos.x += next.x
        pos.y += next.y
        distance += 1

    print(distance // 2)