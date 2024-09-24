# Advent of Code 2023
# Day 17-1: Clumsy Crucible

from queue import PriorityQueue


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


# Calculate accumulated heat loss for each cell in grid.
def map_heat_loss(grid):
    heat_loss_map = [[{} for _ in range(len(grid[0]))] for _ in grid]

    queue = PriorityQueue()
    queue.put((0, (Vec(0, 0),)))

    while queue.qsize() > 0:
        path = queue.get()
        trace = path[1]
        pos = trace[0]

        if pos.x < 0 or pos.x >= len(grid[0]) or pos.y < 0 or pos.y >= len(grid):
            continue

        heat_loss = path[0]
        if len(trace) > 1:  # Skip first cell.
            heat_loss += grid[pos.y][pos.x]

        # Key with path:
        key = trace
        for i in range(2, len(key)):
            a = trace[i - 2]
            b = trace[i - 1]
            c = trace[i]

            if c.x - b.x != b.x - a.x or c.y - b.y != b.y - a.y:
                key = key[:i]
                break
        key = key[1:]

        # Record smallest value for each path:
        heat_losses = heat_loss_map[pos.y][pos.x]
        if key not in heat_losses or heat_losses[key] > heat_loss:
            heat_losses[key] = heat_loss
        else:
            continue

        go_north = go_east = go_south = go_west = True

        # Path cannot reverse:
        if len(trace) > 1:
            trace1 = trace[1]

            if trace1.y < pos.y:
                go_north = False
            if trace1.x > pos.x:
                go_east = False
            if trace1.y > pos.y:
                go_south = False
            if trace1.x < pos.x:
                go_west = False

        # Path cannot go straight more than 3 steps:
        if len(trace) > 3:
            trace3 = trace[3]

            if trace3.y == pos.y + 3:
                go_north = False
            if trace3.x == pos.x - 3:
                go_east = False
            if trace3.y == pos.y - 3:
                go_south = False
            if trace3.x == pos.x + 3:
                go_west = False

        if go_north:
            queue.put((heat_loss, (Vec(pos.x, pos.y - 1),) + trace[:min(3, len(trace))]))
        if go_east:
            queue.put((heat_loss, (Vec(pos.x + 1, pos.y),) + trace[:min(3, len(trace))]))
        if go_south:
            queue.put((heat_loss, (Vec(pos.x, pos.y + 1),) + trace[:min(3, len(trace))]))
        if go_west:
            queue.put((heat_loss, (Vec(pos.x - 1, pos.y),) + trace[:min(3, len(trace))]))

    return heat_loss_map


def parse_input(path):
    with open(path) as file:
        return [[int(x) for x in line.strip()] for line in file.readlines()]


grid = parse_input("input.txt")
heat_loss_map = map_heat_loss(grid)

# Find the smallest heat loss:
min_heat_loss = float("inf")
for cell in heat_loss_map[-1][-1]:
    min_heat_loss = min(heat_loss_map[-1][-1][cell], min_heat_loss)

print(min_heat_loss)