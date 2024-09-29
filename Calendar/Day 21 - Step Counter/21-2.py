# Advent of Code 2023
# Day 21-2: Step Counter

N = 26501365

PLOT = "."
ROCK = "#"
START = "S"
VISIT = "O"

MOVES = ((1, 0), (0, 1), (-1, 0), (0, -1))


class Grid:
    def __init__(self, template):
        self.template = template
        self.template_width = len(template[0])
        self.template_height = len(template)

        self.grid = [row.copy() for row in template]
        self.width, self.height = len(self.grid[0]), len(self.grid)
        self.dx = self.dy = 0

        self.mod_count = 0

    def get(self, x, y):
        self.extend(x, y)

        return self.grid[y + self.dy][x + self.dx]

    def set(self,x, y, value):
        self.extend(x, y)

        if value != self.get(x, y):
            self.mod_count += 1

        self.grid[y + self.dy][x + self.dx] = value

    def extend(self, x, y):
        while y + self.dy < 0:
            self.height += self.template_height
            self.dy += self.template_height
            self.grid = [row * (self.width // self.template_width) for row in self.template] + self.grid

        while y + self.dy >= self.height:
            self.height += self.template_height
            self.grid += [row * (self.width // self.template_width) for row in self.template]

        while x + self.dx < 0:
            self.width += self.template_width
            self.dx += self.template_width
            for y in range(self.height):
                self.grid[y] = self.template[y % self.template_height] + self.grid[y]

        while x + self.dx >= self.width:
            self.width += self.template_width
            for y in range(self.height):
                self.grid[y] += self.template[y % self.template_height]


def prepare_grids(template, start):
    evens = Grid(template)
    odds = Grid(template)

    evens.set(start[0], start[1], VISIT)
    odds.set(start[0], start[1], PLOT)

    return evens, odds


def parse_input(path):
    with open(path) as file:
        grid = [list(row.strip()) for row in file.readlines()]

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == START:
                    grid[y][x] = PLOT
                    return grid, (x, y)


template, start = parse_input("input.txt")
evens, odds = prepare_grids(template, start)
evens_queue, odds_queue = [start], []

rep = len(template)
delta_edge_counts = []
mod_count = 1

for i in range(N):
    perfect_edge_count = pow(i + 2, 2) - pow(i + 1, 2)

    if i >= 2 * rep:  # After 2N steps, use pattern:
        delta_edge_count_start = delta_edge_counts[i % rep]
        delta_edge_count_period = delta_edge_counts[i % rep + rep] - delta_edge_count_start
        period_count = i // rep

        delta_edge_count = delta_edge_count_start + period_count * delta_edge_count_period
        actual_edge_count = perfect_edge_count - delta_edge_count

        mod_count += actual_edge_count
    else:  # Before 2N, fill grids to find pattern:
        from_grid = evens if i % 2 == 0 else odds
        to_grid = evens if i % 2 == 1 else odds

        from_queue = evens_queue if i % 2 == 0 else odds_queue
        to_queue = evens_queue if i % 2 == 1 else odds_queue

        while len(from_queue) > 0:
            visit = from_queue.pop(0)

            for move in MOVES:
                move_x = visit[0] + move[0]
                move_y = visit[1] + move[1]

                if to_grid.get(move_x, move_y) == PLOT:
                    to_grid.set(move_x, move_y, VISIT)
                    to_queue.append((move_x, move_y))

        actual_edge_count = to_grid.mod_count - from_grid.mod_count
        mod_count += actual_edge_count

        delta_edge_counts.append(perfect_edge_count - actual_edge_count)

grid = evens if N % 2 == 0 else odds

print(mod_count)