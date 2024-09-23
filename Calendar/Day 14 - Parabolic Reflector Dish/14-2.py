# Advent of Code 2023
# Day 14-2: Parabolic Reflector Dish

N_CYCLES = 1_000_000_000

ROUND_ROCK = "O"
BLOCK_ROCK = "#"
EMPTY = "."


def parse_input(path):
    with open(path) as file:
        return [list(line.strip()) for line in file.readlines()]


def run_tilt_cycles(platform, n_cycles):
    snapshot = get_snapshot(platform)
    snapshots = [snapshot]

    while True:
        tilt_cycle(platform)
        snapshot = get_snapshot(platform)

        if snapshot in snapshots:
            break
        else:
            snapshots.append(snapshot)

    period_start = len(snapshots)
    period_length = len(snapshots) - snapshots.index(snapshot)
    remaining = (n_cycles - period_start) % period_length

    for i in range(remaining):
        tilt_cycle(platform)


def tilt_cycle(platform):
    tilt_vertical(platform, range(len(platform))) # North
    tilt_horizontal(platform, range(len(platform[0]))) # West
    tilt_vertical(platform, range(len(platform) - 1, -1, -1)) # South
    tilt_horizontal(platform, range(len(platform[0]) - 1, -1, -1)) # East


def tilt_vertical(platform, range):
    for x in range:
        i = 0

        while i < len(range):
            y0 = range[i]
            y1 = range[max(i - 1, 0)]

            if i > 0 and platform[y0][x] == ROUND_ROCK and platform[y1][x] == EMPTY:
                platform[y0][x], platform[y1][x] = platform[y1][x], platform[y0][x]
                i -= 1
            else:
                i += 1


def tilt_horizontal(platform, range):
    for y in range:
        i = 0

        while i < len(range):
            x0 = range[i]
            x1 = range[max(i - 1, 0)]

            if i > 0 and platform[y][x0] == ROUND_ROCK and platform[y][x1] == EMPTY:
                platform[y][x0], platform[y][x1] = platform[y][x1], platform[y][x0]
                i -= 1
            else:
                i += 1


def get_snapshot(platform):
    num = "".join(["".join(x) for x in platform])
    num = num.replace(ROUND_ROCK, "1").replace(BLOCK_ROCK, "0").replace(EMPTY, "0")

    return int("0b" + num, 2)


def count_load(platform):
    sum = 0

    for y in range(len(platform)):
        sum += (len(platform) - y) * platform[y].count(ROUND_ROCK)

    return sum


platform = parse_input("input.txt")
run_tilt_cycles(platform, N_CYCLES)

print(count_load(platform))