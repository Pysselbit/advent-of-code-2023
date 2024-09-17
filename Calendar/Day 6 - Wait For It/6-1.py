# Advent of Code 2023
# Day 6-1: Wait For It

import re


class Race:
    def __init__(self, time, distance):
        self.time = time
        self.distance = distance


def parse_races(lines):
    times = re.findall(r"\d+", lines[0])
    distances = re.findall(r"\d+", lines[1])
    races = []

    for i in range(len(times)):
        races.append(Race(int(times[i]), int(distances[i])))

    return races


with open("input.txt") as file:
    races = parse_races(file.readlines())
    total_wins = 1

    for race in races:
        wins = 0

        for speed in range(race.time):
            time = race.time - speed
            distance = time * speed

            if distance > race.distance:
                wins += 1

        total_wins *= wins

    print(total_wins)