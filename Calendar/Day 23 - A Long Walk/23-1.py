# Advent of Code 2023
# Day 23-1: A Long Walk

UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)

DIRECTIONS = (UP, RIGHT, DOWN, LEFT)


class Walker:
    def __init__(self, grid, x, y, x0, y0, distance):
        self.grid = grid

        self.x, self.y = x, y
        self.x0, self.y0 = x0, y0

        self.distance = distance

    def can_walk(self, dx, dy):
        x = self.x + dx
        y = self.y + dy

        if x == self.x0 and y == self.y0:
            return False

        cell = grid[self.y][self.x]
        next_cell = grid[y][x]
        direction = (dx, dy)

        # Must align with slopes:
        if cell in "^>v<":
            if cell == "^" and direction != UP:
                return False
            if cell == ">" and direction != RIGHT:
                return False
            if cell == "v" and direction != DOWN:
                return False
            if cell == "<" and direction != LEFT:
                return False

        # Cannot move against slopes:
        if next_cell in "^>v<":
            if next_cell == "^" and direction == DOWN:
                return False
            if next_cell == ">" and direction == LEFT:
                return False
            if next_cell == "v" and direction == UP:
                return False
            if next_cell == "<" and direction == RIGHT:
                return False

            return True

        return next_cell == "."

    def walk(self, dx, dy):
        self.x0, self.y0 = self.x, self.y

        self.x += dx
        self.y += dy

        self.distance += 1


with open("input.txt") as file:
    grid = [row.strip() for row in file.readlines()]
    walkers = [Walker(grid, 1, 0, 1, -1, 0)]
    max_distance = 0

    goal_x = len(grid[0]) - 2
    goal_y = len(grid) - 1

    while len(walkers) > 0:
        clone_walkers = []
        finished_walkers = []

        for walker in walkers:
            valid_directions = []

            # Find valid directions:
            for direction in DIRECTIONS:
                if walker.can_walk(direction[0], direction[1]):
                    valid_directions.append(direction)

            # Remove dead ends:
            if len(valid_directions) == 0:
                finished_walkers.append(walker)

            # Move along valid direction (and clone if more than one direction):
            for i in range(len(valid_directions)):
                dx, dy = valid_directions[i][0], valid_directions[i][1]

                if i < len(valid_directions) - 1:
                    clone_walker = Walker(grid, walker.x + dx, walker.y + dy, walker.x, walker.y, walker.distance + 1)
                    clone_walkers.append(clone_walker)
                else:
                    walker.walk(dx, dy)

        # Add new clones:
        walkers.extend(clone_walkers)

        # Find walkers that reached the goal:
        for walker in walkers:
            if walker.x == goal_x and walker.y == goal_y:
                max_distance = max(walker.distance, max_distance)
                finished_walkers.append(walker)

        # Remove finished and dead-end walkers:
        for finished_walker in finished_walkers:
            walkers.remove(finished_walker)

    print(max_distance)