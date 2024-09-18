# Advent of Code 2023
# Day 8-1: Haunted Wasteland

import re

START = "AAA"
FINISH = "ZZZ"

with open("input.txt") as file:
    lines = file.readlines()

    moves = lines[0].strip()
    graph = {}

    for i in range(2, len(lines)):
        matches = re.findall(r"[A-Z][A-Z][A-Z]", lines[i])
        graph[matches[0]] = [matches[1], matches[2]]

    move_index = 0
    move_count = 0
    node = START

    while node != FINISH:
        move = moves[move_index]
        node = graph[node][0] if move == "L" else graph[node][1]

        move_index = (move_index + 1) % len(moves)
        move_count += 1

    print(move_count)