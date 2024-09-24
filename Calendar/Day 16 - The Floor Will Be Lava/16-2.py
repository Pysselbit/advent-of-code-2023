# Advent of Code 2023
# Day 16-2: The Floor Will Be Lava

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


def sum_energized_cells(grid, start_ray):
    width, height = len(grid[0]), len(grid)
    energized_grid = [[[] for _ in range(width)] for _ in range(height)]
    rays = [start_ray]

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

    return sum([sum([1 for cell in row if len(cell) > 0]) for row in energized_grid])


with open("input.txt") as file:
    grid = [line.strip() for line in file.readlines()]
    rays = []

    for x in range(len(grid[0])):
        rays.append(Ray(x, -1, 0, 1))
        rays.append(Ray(x, len(grid), 0, -1))
    for y in range(len(grid)):
        rays.append(Ray(-1, y, 1, 0))
        rays.append(Ray(len(grid[y]), y, -1, 0))

    max_sum = 0
    for ray in rays:
        max_sum = max(sum_energized_cells(grid, ray), max_sum)

    print(max_sum)