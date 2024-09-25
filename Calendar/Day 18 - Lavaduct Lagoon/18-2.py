# Advent of Code 2023
# Day 18-2: Lavaduct Lagoon

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3


class Command:
    def __init__(self, input):
        self.direction = int(input[7:8])
        self.steps = int(input[2:7], 16)


# Get area using shoelace formula.
def get_area(commands):
    area = 0
    circumference = 0
    v0 = (0, 0)

    for command in commands:
        steps = command.steps
        dx = steps if command.direction == RIGHT else -steps if command.direction == LEFT else 0
        dy = steps if command.direction == DOWN else -steps if command.direction == UP else 0

        v1 = (v0[0] + dx, v0[1] + dy)
        area += v0[0] * v1[1] - v0[1] * v1[0]
        circumference += steps
        v0 = v1

    return (area + circumference) // 2 + 1


def parse_input(path):
    with open(path) as file:
        commands = []

        for row in [line.strip().split(" ") for line in file.readlines()]:
            commands.append(Command(row[-1]))

        return commands


commands = parse_input("input.txt")
print(get_area(commands))