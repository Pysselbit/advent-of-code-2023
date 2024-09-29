# Advent of Code 2023
# Day 21-1: Step Counter

N = 64

PLOT = "."
ROCK = "#"
START = "S"
VISIT = "O"

MOVES = ((1, 0), (0, 1), (-1, 0), (0, -1))


def parse_input(path):
    with open(path) as file:
        evens = [list(row.strip()) for row in file.readlines()]
        odds = [row.copy() for row in evens]

        for y in range(len(evens)):
            for x in range(len(evens[y])):
                if evens[y][x] == START:
                    evens[y][x] = VISIT
                    odds[y][x] = PLOT

        return evens, odds


evens, odds = parse_input("input.txt")
width, height = len(evens[0]), len(evens)

for i in range(N):
    from_grid = evens if i % 2 == 0 else odds
    to_grid = evens if i % 2 == 1 else odds

    for y in range(height):
        for x in range(width):
            if from_grid[y][x] == VISIT:
                for move in MOVES:
                    move_x = x + move[0]
                    move_y = y + move[1]

                    if not (0 <= move_x < width and 0 <= move_y < height):
                        continue

                    if to_grid[move_y][move_x] == PLOT:
                        to_grid[move_y][move_x] = VISIT

grid = evens if N % 2 == 0 else odds

print(sum([row.count(VISIT) for row in grid]))
