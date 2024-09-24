# Advent of Code 2023
# Day 16-1: The Floor Will Be Lava

class Ray:
    def __init__(self, x, y, dx, dy):
        self.x, self.y = x, y
        self.dx, self.dy = dx, dy


class Direction:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def __eq__(self, other):
        return other.dx == self.dx and other.dy == self.dy


with open("input.txt") as file:
    grid = [line.strip() for line in file.readlines()]
    width, height = len(grid[0]), len(grid)

    energized_grid = [[[] for _ in range(width)] for _ in range(height)]
    rays = [Ray(-1, 0, 1, 0)]

    while len(rays) > 0:
        i = 0
        while i < len(rays):
            ray = rays[i]

            ray.x += ray.dx
            ray.y += ray.dy

            if ray.x < 0 or ray.x >= width or ray.y < 0 or ray.y >= height:
                rays.remove(ray)
                continue

            direction = Direction(ray.dx, ray.dy)
            if direction in energized_grid[ray.y][ray.x]:
                rays.remove(ray)
                continue
            else:
                energized_grid[ray.y][ray.x].append(direction)

            cell = grid[ray.y][ray.x]
            if cell == "\\":
                ray.dx, ray.dy = ray.dy, ray.dx
            elif cell == "/":
                ray.dx, ray.dy = -ray.dy, -ray.dx
            elif cell == "|" and ray.dx != 0 or cell == "-" and ray.dy != 0:
                ray.dx, ray.dy = ray.dy, ray.dx
                rays.insert(0, Ray(ray.x, ray.y, -ray.dx, -ray.dy))
                i += 1

            i += 1

    print(sum([sum([1 for cell in row if len(cell) > 0]) for row in energized_grid]))