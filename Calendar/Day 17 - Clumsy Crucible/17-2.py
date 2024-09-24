# Advent of Code 2023
# Day 17-2: Clumsy Crucible

from queue import PriorityQueue

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

HEAT_LOSS = 0
POSITION = 1
DIRECTION = 2
STEPS = 3


class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return other.x == self.x and other.y == self.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return other.x + other.y < self.x + self.y

    def __hash__(self):
        return hash((self.x, self.y))


def turn_right(direction):
    return (direction + 1) % 4


def turn_left(direction):
    return (direction - 1) % 4


def step(pos, direction):
    if direction == NORTH:
        return Vec(pos.x, pos.y - 1)
    if direction == EAST:
        return Vec(pos.x + 1, pos.y)
    if direction == SOUTH:
        return Vec(pos.x, pos.y + 1)
    if direction == WEST:
        return Vec(pos.x - 1, pos.y)


# Calculate accumulated heat loss for each cell in grid.
def map_heat_loss(grid):
    heat_loss_map = [[{} for _ in range(len(grid[0]))] for _ in grid]

    queue = PriorityQueue()
    queue.put((0, Vec(0, 0), None, 0))

    while queue.qsize() > 0:
        item = queue.get()
        heat_loss = item[HEAT_LOSS]
        pos = item[POSITION]
        direction = item[DIRECTION]
        steps = item[STEPS]

        if pos.x < 0 or pos.x >= len(grid[0]) or pos.y < 0 or pos.y >= len(grid):
            continue

        if steps > 0:  # Skip first cell.
            heat_loss += grid[pos.y][pos.x]

        # Record smallest value for each path:
        key = (direction, steps)
        heat_losses = heat_loss_map[pos.y][pos.x]
        if key not in heat_losses or heat_losses[key] > heat_loss:
            heat_losses[key] = heat_loss
        else:
            continue

        # Path has to go straight 4 <= n <= 10 steps:
        next_directions = []
        if direction is None:  # First item has no direction.
            next_directions.extend([EAST, SOUTH])
        else:
            if steps < 10:
                next_directions.append(direction)
            if steps >= 4:
                next_directions.append(turn_right(direction))
                next_directions.append(turn_left(direction))

        for next_direction in next_directions:
            next_pos = step(pos, next_direction)
            next_steps = steps + 1 if next_direction == direction else 1

            queue.put((heat_loss, next_pos, next_direction, next_steps))

    return heat_loss_map


def parse_input(path):
    with open(path) as file:
        return [[int(x) for x in line.strip()] for line in file.readlines()]


grid = parse_input("input.txt")
heat_loss_map = map_heat_loss(grid)

# Find the smallest heat loss:
min_heat_loss = float("inf")
for cell in heat_loss_map[-1][-1]:
    if cell[1] >= 4:  # Min 4 straight steps to finish.
        min_heat_loss = min(heat_loss_map[-1][-1][cell], min_heat_loss)

print(min_heat_loss)
