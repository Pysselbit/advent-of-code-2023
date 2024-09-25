# Advent of Code 2023
# Day 18-1: Lavaduct Lagoon

RIGHT = "R"
DOWN = "D"
LEFT = "L"
UP = "U"


class Command:
    def __init__(self, direction, steps):
        self.direction = direction
        self.steps = steps


class Ground:
    def __init__(self):
        self.grid = [[False]]
        self.width = self.height = 1

    def get(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False

        return self.grid[y][x]

    def set(self, x, y, value):
        if x < 0 or y < 0:
            return

        while y >= self.height:
            self.grid.append([False] * self.width)
            self.height += 1

        while x >= self.width:
            for row in self.grid:
                row.append(False)
            self.width += 1

        self.grid[y][x] = value


def run_commands(ground, commands):
    x, y = get_start_pos(commands)
    ground.set(x, y, True)

    for command in commands:
        steps = command.steps

        dx = 1 if command.direction == RIGHT else -1 if command.direction == LEFT else 0
        dy = 1 if command.direction == DOWN else -1 if command.direction == UP else 0

        while steps > 0:
            x += dx
            y += dy

            ground.set(x, y, True)

            steps -= 1


def get_start_pos(commands):
    x = y = 0
    x_min = y_min = 0

    for command in commands:
        steps = command.steps

        dx = 1 if command.direction == RIGHT else -1 if command.direction == LEFT else 0
        dy = 1 if command.direction == DOWN else -1 if command.direction == UP else 0

        while steps > 0:
            x += dx
            y += dy

            x_min = min(x, x_min)
            y_min = min(y, y_min)

            steps -= 1

    return -x_min, -y_min


def fill_interior(ground):
    start_x, start_y = find_interior(ground)

    queue = [(start_x, start_y)]
    visited = [[False] * ground.width for _ in range(ground.height)]

    while len(queue) > 0:
        pos = queue.pop(0)
        x, y = pos[0], pos[1]

        if 0 <= x < ground.width and 0 <= y < ground.height:
            visited[y][x] = True

            if not ground.get(x, y):
                ground.set(x, y, True)

                if x + 1 < ground.width and not visited[y][x + 1]:
                    queue.append((x + 1, y))
                if x - 1 > 0 and not visited[y][x - 1]:
                    queue.append((x - 1, y))
                if y + 1 < ground.height and not visited[y + 1][x]:
                    queue.append((x, y + 1))
                if y - 1 > 0 and not visited[y - 1][x]:
                    queue.append((x, y - 1))


def find_interior(ground):
    for y in range(ground.height):
        for x in range(2, ground.width):
            if x - 2 == 0 and ground.get(x - 2, y) and not ground.get(x - 1, y):
                return x - 1, y
            if not ground.get(x - 2, y) and ground.get(x - 1, y) and not ground.get(x, y):
                return x, y


def count_fill(ground):
    count = 0

    for y in range(ground.height):
        for x in range(ground.width):
            if ground.get(x, y):
                count += 1

    return count


def parse_input(path):
    with open(path) as file:
        commands = []
        for row in [line.strip().split(" ") for line in file.readlines()]:
            commands.append(Command(row[0], int(row[1])))

        return commands


commands = parse_input("input.txt")
ground = Ground()
run_commands(ground, commands)
fill_interior(ground)

print(count_fill(ground))