# Advent of Code 2023
# Day 10-2: Pipe Maze

class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y


NORTH = Vec(0, -1)
EAST = Vec(1, 0)
SOUTH = Vec(0, 1)
WEST = Vec(-1, 0)

DIRECTIONS = [NORTH, EAST, SOUTH, WEST]

LOOP = "X"
INNER = "I"
OUTER = "O"
TEMP = "T"


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


def get_loop(grid):
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

    loop = [Vec(pos.x, pos.y)]
    pos.x += next.x
    pos.y += next.y

    # Find loop:
    while grid[pos.y][pos.x] != "S":
        for direction in DIRECTIONS:
            if direction.x == -next.x and direction.y == 0 or direction.y == -next.y and direction.x == 0:
                continue

            if has_exit(grid, pos.x, pos.y, direction.x, direction.y):
                next = direction
                break

        loop.append(Vec(pos.x, pos.y))
        pos.x += next.x
        pos.y += next.y

    return loop


def mark(grid, x, y, mark):
    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
        return

    if grid[y][x] != LOOP:
        grid[y][x] = mark


def mark_connected(grid, x, y, mark):
    visited = [[False] * len(grid[0]) for x in range(len(grid))]
    queue = [Vec(x, y)]
    grid[y][x] = TEMP

    while len(queue) > 0:
        pos = queue.pop(0)
        x = pos.x
        y = pos.y

        if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
            continue

        if visited[y][x] or grid[y][x] in [LOOP, INNER, OUTER]:
            continue

        grid[y][x] = mark
        visited[y][x] = True

        queue.append(Vec(x + 1, y))
        queue.append(Vec(x - 1, y))
        queue.append(Vec(x, y + 1))
        queue.append(Vec(x, y - 1))


with open("input.txt") as file:
    grid = [x.strip() for x in file.readlines()]
    meta_grid = [list(x) for x in grid]
    loop = get_loop(grid)

    # Mark loop:
    for pos in loop:
        meta_grid[pos.y][pos.x] = LOOP

    # Mark inner and outer borders:
    for i in range(len(loop)):
        pos = loop[i]
        next_pos = loop[(i + 1) % len(loop)]

        if next_pos.y < pos.y:  # Up
            inner = Vec(1, 0)
            outer = Vec(-1, 0)
        elif next_pos.x > pos.x:  # Right
            inner = Vec(0, 1)
            outer = Vec(0, -1)
        elif next_pos.y > pos.y:  # Down
            inner = Vec(-1, 0)
            outer = Vec(1, 0)
        elif next_pos.x < pos.x:  # Left
            inner = Vec(0, -1)
            outer = Vec(0, 1)

        inners = [Vec(pos.x + inner.x, pos.y + inner.y), Vec(next_pos.x + inner.x, next_pos.y + inner.y)]
        outers = [Vec(pos.x + outer.x, pos.y + outer.y), Vec(next_pos.x + outer.x, next_pos.y + outer.y)]

        for j in range(2):
            mark(meta_grid, inners[j].x, inners[j].y, INNER)
            mark(meta_grid, outers[j].x, outers[j].y, OUTER)

    # Fill empty areas:
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if meta_grid[y][x] == INNER:
                mark_connected(meta_grid, x, y, INNER)
            elif meta_grid[y][x] == OUTER:
                mark_connected(meta_grid, x, y, OUTER)

    # Check if inverted:
    is_inverted = False
    for y in range(len(grid)):
        if y == 0 or y == len(grid) - 1:
            for x in range(len(grid[0])):
                if meta_grid[y][x] == INNER:
                    is_inverted = True

            if meta_grid[y][0] == INNER or meta_grid[y][-1] == INNER:
                is_inverted = True

    # Count inside area:
    print(sum(x.count(INNER if not is_inverted else OUTER) for x in meta_grid))