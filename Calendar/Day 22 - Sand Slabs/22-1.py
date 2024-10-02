# Advent of Code 2023
# Day 22-1: Sand Slabs

class Vec:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Brick:
    def __init__(self, id, min, max):
        self.id = id
        self.min = min
        self.max = max


class Grid:
    def __init__(self, bricks):
        size = Vec(0, 0, 0)

        for brick in bricks:
            size.x = max(brick.max.x + 1, size.x)
            size.y = max(brick.max.y + 1, size.y)
            size.z = max(brick.max.z + 1, size.z)

        self.grid = [[[0 for _ in range(size.x)] for _ in range(size.y)] for _ in range(size.z)]
        self.size = size

        for brick in bricks:
            self.set_brick(brick)

    def set_brick(self, brick):
        for x in range(brick.min.x, brick.max.x + 1):
            for y in range(brick.min.y, brick.max.y + 1):
                for z in range(brick.min.z, brick.max.z + 1):
                    self.grid[z][y][x] = brick.id

    def can_fall(self, brick, ignore_brick=0):
        z = brick.min.z - 1

        if z == 0:
            return False

        for x in range(brick.min.x, brick.max.x + 1):
            for y in range(brick.min.y, brick.max.y + 1):
                if self.grid[z][y][x] != 0 and self.grid[z][y][x] != ignore_brick:
                    return False

        return True

    def fall(self, brick):
        brick.min.z -= 1
        brick.max.z -= 1

        for x in range(brick.min.x, brick.max.x + 1):
            for y in range(brick.min.y, brick.max.y + 1):
                self.grid[brick.max.z + 1][y][x] = 0
                self.grid[brick.min.z][y][x] = brick.id


def parse_input(path):
    with open(path) as file:
        bricks = []

        for line in [x.strip() for x in file.readlines()]:
            nums = ",".join(line.split("~")).split(",")

            min = Vec(int(nums[0]), int(nums[1]), int(nums[2]))
            max = Vec(int(nums[3]), int(nums[4]), int(nums[5]))

            bricks.append(Brick(len(bricks) + 1, min, max))

    return bricks


bricks = parse_input("input.txt")
grid = Grid(bricks)

# Make bricks fall into place:
is_falling = True
while is_falling:
    is_falling = False

    for brick in bricks:
        while grid.can_fall(brick):
            grid.fall(brick)
            is_falling = True

# Check which bricks can be safely disintegrated:
disintegration_count = 0
for brick_a in bricks:
    can_disintegrate = True

    for brick_b in bricks:
        if grid.can_fall(brick_b, brick_a.id):
            can_disintegrate = False
            break

    if can_disintegrate:
        disintegration_count += 1

print(disintegration_count)